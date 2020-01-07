# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import cutword_rpc_pb2 as cutword__rpc__pb2


class CutStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.DoCut = channel.unary_unary(
        '/cutword.Cut/DoCut',
        request_serializer=cutword__rpc__pb2.Data.SerializeToString,
        response_deserializer=cutword__rpc__pb2.Data.FromString,
        )


class CutServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def DoCut(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CutServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'DoCut': grpc.unary_unary_rpc_method_handler(
          servicer.DoCut,
          request_deserializer=cutword__rpc__pb2.Data.FromString,
          response_serializer=cutword__rpc__pb2.Data.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'cutword.Cut', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
