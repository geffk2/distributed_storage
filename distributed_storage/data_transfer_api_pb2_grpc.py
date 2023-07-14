# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import data_transfer_api_pb2 as data__transfer__api__pb2


class KeyValueServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetValue = channel.unary_unary(
                '/data_transfer_api.KeyValueService/GetValue',
                request_serializer=data__transfer__api__pb2.GetValueRequest.SerializeToString,
                response_deserializer=data__transfer__api__pb2.GetValueResponse.FromString,
                )
        self.StoreValue = channel.unary_unary(
                '/data_transfer_api.KeyValueService/StoreValue',
                request_serializer=data__transfer__api__pb2.StoreValueRequest.SerializeToString,
                response_deserializer=data__transfer__api__pb2.StoreValueResponse.FromString,
                )


class KeyValueServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetValue(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StoreValue(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KeyValueServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetValue': grpc.unary_unary_rpc_method_handler(
                    servicer.GetValue,
                    request_deserializer=data__transfer__api__pb2.GetValueRequest.FromString,
                    response_serializer=data__transfer__api__pb2.GetValueResponse.SerializeToString,
            ),
            'StoreValue': grpc.unary_unary_rpc_method_handler(
                    servicer.StoreValue,
                    request_deserializer=data__transfer__api__pb2.StoreValueRequest.FromString,
                    response_serializer=data__transfer__api__pb2.StoreValueResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'data_transfer_api.KeyValueService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class KeyValueService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetValue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/data_transfer_api.KeyValueService/GetValue',
            data__transfer__api__pb2.GetValueRequest.SerializeToString,
            data__transfer__api__pb2.GetValueResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StoreValue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/data_transfer_api.KeyValueService/StoreValue',
            data__transfer__api__pb2.StoreValueRequest.SerializeToString,
            data__transfer__api__pb2.StoreValueResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
