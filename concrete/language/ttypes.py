#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style,utf8strings
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import concrete.metadata.ttypes
import concrete.uuid.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class LanguageIdentification(object):
  """
  A theory about what languages are present in a given communication
  or piece of communication.  Note that it is possible to have more
  than one language present in a given communication.

  Attributes:
   - uuid: Unique identifier for this language identification.
   - metadata: Information about where this language identification came from.
   - languageToProbabilityMap: A list mapping from a language to the probability that that
  language occurs in a given communication.  Each language code should
  occur at most once in this list.  The probabilities do <i>not</i>
  need to sum to one -- for example, if a single communication is known
  to contain both English and French, then it would be appropriate
  to assign a probability of 1 to both langauges.  (Manually
  annotated LanguageProb objects should always have probabilities
  of either zero or one; machine-generated LanguageProbs may have
  intermediate probabilities.)

  Note: The string key should represent the ISO 639-3 three-letter code.
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'uuid', (concrete.uuid.ttypes.UUID, concrete.uuid.ttypes.UUID.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'metadata', (concrete.metadata.ttypes.AnnotationMetadata, concrete.metadata.ttypes.AnnotationMetadata.thrift_spec), None, ), # 2
    (3, TType.MAP, 'languageToProbabilityMap', (TType.STRING,None,TType.DOUBLE,None), None, ), # 3
  )

  def __init__(self, uuid=None, metadata=None, languageToProbabilityMap=None,):
    self.uuid = uuid
    self.metadata = metadata
    self.languageToProbabilityMap = languageToProbabilityMap

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.uuid = concrete.uuid.ttypes.UUID()
          self.uuid.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.metadata = concrete.metadata.ttypes.AnnotationMetadata()
          self.metadata.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.MAP:
          self.languageToProbabilityMap = {}
          (_ktype1, _vtype2, _size0 ) = iprot.readMapBegin()
          for _i4 in xrange(_size0):
            _key5 = iprot.readString().decode('utf-8')
            _val6 = iprot.readDouble();
            self.languageToProbabilityMap[_key5] = _val6
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('LanguageIdentification')
    if self.uuid is not None:
      oprot.writeFieldBegin('uuid', TType.STRUCT, 1)
      self.uuid.write(oprot)
      oprot.writeFieldEnd()
    if self.metadata is not None:
      oprot.writeFieldBegin('metadata', TType.STRUCT, 2)
      self.metadata.write(oprot)
      oprot.writeFieldEnd()
    if self.languageToProbabilityMap is not None:
      oprot.writeFieldBegin('languageToProbabilityMap', TType.MAP, 3)
      oprot.writeMapBegin(TType.STRING, TType.DOUBLE, len(self.languageToProbabilityMap))
      for kiter7,viter8 in self.languageToProbabilityMap.items():
        oprot.writeString(kiter7.encode('utf-8'))
        oprot.writeDouble(viter8)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.uuid is None:
      raise TProtocol.TProtocolException(message='Required field uuid is unset!')
    if self.metadata is None:
      raise TProtocol.TProtocolException(message='Required field metadata is unset!')
    if self.languageToProbabilityMap is None:
      raise TProtocol.TProtocolException(message='Required field languageToProbabilityMap is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.uuid)
    value = (value * 31) ^ hash(self.metadata)
    value = (value * 31) ^ hash(self.languageToProbabilityMap)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
