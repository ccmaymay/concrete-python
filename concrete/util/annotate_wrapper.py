from ..annotate import (
    AnnotateCommunicationBatchService,
    AnnotateCommunicationService,
    AnnotateWithContextService)
from .service_wrapper import (
    ConcreteServiceClientWrapper,
    ConcreteServiceWrapper,
    HTTPConcreteServiceClientWrapper,
    SubprocessConcreteServiceWrapper)


# AnnotateCommunicationBatchService wrappers

AnnotateCommunicationBatchClientWrapper = type(
    'AnnotateCommunicationBatchClientWrapper',
    (ConcreteServiceClientWrapper,),
    {'concrete_service_class': AnnotateCommunicationBatchService})


AnnotateCommunicationBatchServiceWrapper = type(
    'AnnotateCommunicationBatchServiceWrapper',
    (ConcreteServiceWrapper,),
    {'concrete_service_class': AnnotateCommunicationBatchService})


HTTPAnnotateCommunicationBatchClientWrapper = type(
    'HTTPAnnotateCommunicationBatchClientWrapper',
    (HTTPConcreteServiceClientWrapper,),
    {'concrete_service_class': AnnotateCommunicationBatchService})


SubprocessAnnotateCommunicationBatchServiceWrapper = type(
    'SubprocessAnnotateCommunicationBatchServiceWrapper',
    (SubprocessConcreteServiceWrapper,),
    {'concrete_service_wrapper_class': AnnotateCommunicationBatchServiceWrapper})


# AnnotateCommunicationService wrappers

AnnotateCommunicationClientWrapper = type(
    'AnnotateCommunicationClientWrapper',
    (ConcreteServiceClientWrapper,),
    {'concrete_service_class': AnnotateCommunicationService})


AnnotateCommunicationServiceWrapper = type(
    'AnnotateCommunicationServiceWrapper',
    (ConcreteServiceWrapper,),
    {'concrete_service_class': AnnotateCommunicationService})


HTTPAnnotateCommunicationClientWrapper = type(
    'HTTPAnnotateCommunicationClientWrapper',
    (HTTPConcreteServiceClientWrapper,),
    {'concrete_service_class': AnnotateCommunicationService})


SubprocessAnnotateCommunicationServiceWrapper = type(
    'SubprocessAnnotateCommunicationServiceWrapper',
    (SubprocessConcreteServiceWrapper,),
    {'concrete_service_wrapper_class': AnnotateCommunicationServiceWrapper})


# AnnotateWithContextService wrappers

AnnotateWithContextClientWrapper = type(
    'AnnotateWithContextClientWrapper',
    (ConcreteServiceClientWrapper,),
    {'concrete_service_class': AnnotateWithContextService})


AnnotateWithContextServiceWrapper = type(
    'AnnotateWithContextServiceWrapper',
    (ConcreteServiceWrapper,),
    {'concrete_service_class': AnnotateWithContextService})


HTTPAnnotateWithContextClientWrapper = type(
    'HTTPAnnotateWithContextClientWrapper',
    (HTTPConcreteServiceClientWrapper,),
    {'concrete_service_class': AnnotateWithContextService})


SubprocessAnnotateWithContextServiceWrapper = type(
    'SubprocessAnnotateWithContextServiceWrapper',
    (SubprocessConcreteServiceWrapper,),
    {'concrete_service_wrapper_class': AnnotateWithContextServiceWrapper})
