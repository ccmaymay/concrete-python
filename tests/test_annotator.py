#!/usr/bin/env python

from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift.protocol import TCompactProtocol

import unittest

from concrete.services import Annotator

from concrete.util.annotator_wrapper import SubprocessAnnotatorServiceWrapper
from concrete.util.net import find_port
from concrete.util.simple_comm import create_simple_comm

from .annotators import NoopAnnotator


class TestAnnotator(unittest.TestCase):
    def test_annotate(self):
        impl = NoopAnnotator()
        host = 'localhost'
        port = find_port()
        timeout = 5

        comm_id = '1-2-3-4'
        comm = create_simple_comm(comm_id)

        comm_uuid_uuidString = comm.uuid.uuidString
        comm_metadata_tool = comm.metadata.tool
        comm_metadata_timestamp = comm.metadata.timestamp

        with SubprocessAnnotatorServiceWrapper(impl, host, port, timeout=timeout) as w:
            transport = TSocket.TSocket(host, port)
            transport = TTransport.TFramedTransport(transport)
            protocol = TCompactProtocol.TCompactProtocol(transport)

            cli = Annotator.Client(protocol)
            transport.open()
            res = cli.annotate(comm)
            transport.close()

            self.assertEqual(res.id, comm_id)
            self.assertEqual(res.uuid.uuidString, comm_uuid_uuidString)
            self.assertEqual(res.metadata.tool, comm_metadata_tool)
            self.assertEqual(res.metadata.timestamp, comm_metadata_timestamp)

    def test_get_metadata(self):
        impl = NoopAnnotator()
        host = 'localhost'
        port = find_port()
        timeout = 5

        with SubprocessAnnotatorServiceWrapper(impl, host, port, timeout=timeout) as w:
            transport = TSocket.TSocket(host, port)
            transport = TTransport.TFramedTransport(transport)
            protocol = TCompactProtocol.TCompactProtocol(transport)

            cli = Annotator.Client(protocol)
            transport.open()
            metadata = cli.getMetadata()
            transport.close()

            self.assertEqual(NoopAnnotator.METADATA_TOOL, metadata.tool)


if __name__ == '__main__':
    unittest.main(buffer=True)
