from __future__ import unicode_literals
from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift.protocol import TCompactProtocol

from concrete.util import (
    SubprocessAnnotateCommunicationServiceWrapper,
    SubprocessAnnotateCommunicationBatchServiceWrapper,
)
from concrete.util import find_port
from concrete.util import create_comm


from time import time

from concrete.annotate import (
    AnnotateCommunicationService,
    AnnotateCommunicationBatchService,
)
from concrete import AnnotationMetadata


from pytest import mark


class NoopAnnotateCommunicationService(AnnotateCommunicationService.Iface):
    METADATA_TOOL = 'No-op AnnotateCommunicationService'

    def annotate(self, communication):
        return communication

    def getMetadata(self,):
        metadata = AnnotationMetadata(tool=self.METADATA_TOOL,
                                      timestamp=int(time()))
        return metadata

    def getDocumentation(self):
        return '''\
        AnnotateCommunicationService that returns communication unmodified
        '''

    def shutdown(self):
        pass


class NoopAnnotateCommunicationBatchService(AnnotateCommunicationBatchService.Iface):
    METADATA_TOOL = 'No-op AnnotateCommunicationBatchService'

    def annotate(self, communication):
        return self.annotateBatch([communication])[0]

    def annotateBatch(self, communications):
        return communications

    def getMetadata(self,):
        metadata = AnnotationMetadata(tool=self.METADATA_TOOL,
                                      timestamp=int(time()))
        return metadata

    def getDocumentation(self):
        return '''\
        AnnotateCommunicationBatchService that returns communications unmodified
        '''

    def shutdown(self):
        pass


# Test single-communication and batch annotate clients and services
# against each other to test backwards compatibility of batch annotate
# to single-communication annotate.
@mark.parametrize(
    'client_class',
    [
        AnnotateCommunicationService,
        AnnotateCommunicationBatchService,
    ]
)
@mark.parametrize(
    'service_class,service_wrapper_class',
    [
        (
            NoopAnnotateCommunicationService,
            SubprocessAnnotateCommunicationServiceWrapper,
        ),
        (
            NoopAnnotateCommunicationBatchService,
            SubprocessAnnotateCommunicationBatchServiceWrapper,
        ),
    ])
def test_annotate(service_class, service_wrapper_class, client_class):
    impl = service_class()
    host = 'localhost'
    port = find_port()
    timeout = 5

    comm_id = '1-2-3-4'
    comm = create_comm(comm_id)

    comm_uuid_uuidString = comm.uuid.uuidString
    comm_metadata_tool = comm.metadata.tool
    comm_metadata_timestamp = comm.metadata.timestamp

    with service_wrapper_class(impl, host, port, timeout=timeout):
        transport = TSocket.TSocket(host, port)
        transport = TTransport.TFramedTransport(transport)
        protocol = TCompactProtocol.TCompactProtocolAccelerated(transport)

        cli = client_class.Client(protocol)
        transport.open()
        res = cli.annotate(comm)
        transport.close()

        assert res.id == comm_id
        assert res.uuid.uuidString == comm_uuid_uuidString
        assert res.metadata.tool == comm_metadata_tool
        assert res.metadata.timestamp == comm_metadata_timestamp


# Test single-communication and batch annotate clients and services
# against each other to test backwards compatibility of batch annotate
# to single-communication annotate.
@mark.parametrize(
    'client_class',
    [
        AnnotateCommunicationService,
        AnnotateCommunicationBatchService,
    ]
)
@mark.parametrize(
    'service_class,service_wrapper_class',
    [
        (
            NoopAnnotateCommunicationService,
            SubprocessAnnotateCommunicationServiceWrapper,
        ),
        (
            NoopAnnotateCommunicationBatchService,
            SubprocessAnnotateCommunicationBatchServiceWrapper,
        ),
    ])
def test_get_metadata(service_class, service_wrapper_class, client_class):
    impl = service_class()
    host = 'localhost'
    port = find_port()
    timeout = 5

    with service_wrapper_class(impl, host, port, timeout=timeout):
        transport = TSocket.TSocket(host, port)
        transport = TTransport.TFramedTransport(transport)
        protocol = TCompactProtocol.TCompactProtocolAccelerated(transport)

        cli = client_class.Client(protocol)
        transport.open()
        metadata = cli.getMetadata()
        transport.close()

        assert service_class.METADATA_TOOL == metadata.tool
