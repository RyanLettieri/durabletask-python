# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: orchestrator_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aorchestrator_service.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1bgoogle/protobuf/empty.proto\"^\n\x15OrchestrationInstance\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x31\n\x0b\x65xecutionId\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xc2\x01\n\x0f\x41\x63tivityRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12-\n\x07version\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05input\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x15orchestrationInstance\x18\x04 \x01(\x0b\x32\x16.OrchestrationInstance\x12\x0e\n\x06taskId\x18\x05 \x01(\x05\"\x91\x01\n\x10\x41\x63tivityResponse\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0e\n\x06taskId\x18\x02 \x01(\x05\x12,\n\x06result\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x0e\x66\x61ilureDetails\x18\x04 \x01(\x0b\x32\x13.TaskFailureDetails\"\xb2\x01\n\x12TaskFailureDetails\x12\x11\n\terrorType\x18\x01 \x01(\t\x12\x14\n\x0c\x65rrorMessage\x18\x02 \x01(\t\x12\x30\n\nstackTrace\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12)\n\x0cinnerFailure\x18\x04 \x01(\x0b\x32\x13.TaskFailureDetails\x12\x16\n\x0eisNonRetriable\x18\x05 \x01(\x08\"\xbf\x01\n\x12ParentInstanceInfo\x12\x17\n\x0ftaskScheduledId\x18\x01 \x01(\x05\x12*\n\x04name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07version\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x15orchestrationInstance\x18\x04 \x01(\x0b\x32\x16.OrchestrationInstance\"i\n\x0cTraceContext\x12\x13\n\x0btraceParent\x18\x01 \x01(\t\x12\x12\n\x06spanID\x18\x02 \x01(\tB\x02\x18\x01\x12\x30\n\ntraceState\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x88\x03\n\x15\x45xecutionStartedEvent\x12\x0c\n\x04name\x18\x01 \x01(\t\x12-\n\x07version\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05input\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x15orchestrationInstance\x18\x04 \x01(\x0b\x32\x16.OrchestrationInstance\x12+\n\x0eparentInstance\x18\x05 \x01(\x0b\x32\x13.ParentInstanceInfo\x12;\n\x17scheduledStartTimestamp\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12)\n\x12parentTraceContext\x18\x07 \x01(\x0b\x32\r.TraceContext\x12\x39\n\x13orchestrationSpanID\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xa7\x01\n\x17\x45xecutionCompletedEvent\x12\x31\n\x13orchestrationStatus\x18\x01 \x01(\x0e\x32\x14.OrchestrationStatus\x12,\n\x06result\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x0e\x66\x61ilureDetails\x18\x03 \x01(\x0b\x32\x13.TaskFailureDetails\"X\n\x18\x45xecutionTerminatedEvent\x12+\n\x05input\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x0f\n\x07recurse\x18\x02 \x01(\x08\"\xa9\x01\n\x12TaskScheduledEvent\x12\x0c\n\x04name\x18\x01 \x01(\t\x12-\n\x07version\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05input\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12)\n\x12parentTraceContext\x18\x04 \x01(\x0b\x32\r.TraceContext\"[\n\x12TaskCompletedEvent\x12\x17\n\x0ftaskScheduledId\x18\x01 \x01(\x05\x12,\n\x06result\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"W\n\x0fTaskFailedEvent\x12\x17\n\x0ftaskScheduledId\x18\x01 \x01(\x05\x12+\n\x0e\x66\x61ilureDetails\x18\x02 \x01(\x0b\x32\x13.TaskFailureDetails\"\xcf\x01\n$SubOrchestrationInstanceCreatedEvent\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12-\n\x07version\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05input\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12)\n\x12parentTraceContext\x18\x05 \x01(\x0b\x32\r.TraceContext\"o\n&SubOrchestrationInstanceCompletedEvent\x12\x17\n\x0ftaskScheduledId\x18\x01 \x01(\x05\x12,\n\x06result\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"k\n#SubOrchestrationInstanceFailedEvent\x12\x17\n\x0ftaskScheduledId\x18\x01 \x01(\x05\x12+\n\x0e\x66\x61ilureDetails\x18\x02 \x01(\x0b\x32\x13.TaskFailureDetails\"?\n\x11TimerCreatedEvent\x12*\n\x06\x66ireAt\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"N\n\x0fTimerFiredEvent\x12*\n\x06\x66ireAt\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07timerId\x18\x02 \x01(\x05\"\x1a\n\x18OrchestratorStartedEvent\"\x1c\n\x1aOrchestratorCompletedEvent\"_\n\x0e\x45ventSentEvent\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12+\n\x05input\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"M\n\x10\x45ventRaisedEvent\x12\x0c\n\x04name\x18\x01 \x01(\t\x12+\n\x05input\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x1c\n\x0cGenericEvent\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"D\n\x11HistoryStateEvent\x12/\n\x12orchestrationState\x18\x01 \x01(\x0b\x32\x13.OrchestrationState\"A\n\x12\x43ontinueAsNewEvent\x12+\n\x05input\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"F\n\x17\x45xecutionSuspendedEvent\x12+\n\x05input\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"D\n\x15\x45xecutionResumedEvent\x12+\n\x05input\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x86\t\n\x0cHistoryEvent\x12\x0f\n\x07\x65ventId\x18\x01 \x01(\x05\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x10\x65xecutionStarted\x18\x03 \x01(\x0b\x32\x16.ExecutionStartedEventH\x00\x12\x36\n\x12\x65xecutionCompleted\x18\x04 \x01(\x0b\x32\x18.ExecutionCompletedEventH\x00\x12\x38\n\x13\x65xecutionTerminated\x18\x05 \x01(\x0b\x32\x19.ExecutionTerminatedEventH\x00\x12,\n\rtaskScheduled\x18\x06 \x01(\x0b\x32\x13.TaskScheduledEventH\x00\x12,\n\rtaskCompleted\x18\x07 \x01(\x0b\x32\x13.TaskCompletedEventH\x00\x12&\n\ntaskFailed\x18\x08 \x01(\x0b\x32\x10.TaskFailedEventH\x00\x12P\n\x1fsubOrchestrationInstanceCreated\x18\t \x01(\x0b\x32%.SubOrchestrationInstanceCreatedEventH\x00\x12T\n!subOrchestrationInstanceCompleted\x18\n \x01(\x0b\x32\'.SubOrchestrationInstanceCompletedEventH\x00\x12N\n\x1esubOrchestrationInstanceFailed\x18\x0b \x01(\x0b\x32$.SubOrchestrationInstanceFailedEventH\x00\x12*\n\x0ctimerCreated\x18\x0c \x01(\x0b\x32\x12.TimerCreatedEventH\x00\x12&\n\ntimerFired\x18\r \x01(\x0b\x32\x10.TimerFiredEventH\x00\x12\x38\n\x13orchestratorStarted\x18\x0e \x01(\x0b\x32\x19.OrchestratorStartedEventH\x00\x12<\n\x15orchestratorCompleted\x18\x0f \x01(\x0b\x32\x1b.OrchestratorCompletedEventH\x00\x12$\n\teventSent\x18\x10 \x01(\x0b\x32\x0f.EventSentEventH\x00\x12(\n\x0b\x65ventRaised\x18\x11 \x01(\x0b\x32\x11.EventRaisedEventH\x00\x12%\n\x0cgenericEvent\x18\x12 \x01(\x0b\x32\r.GenericEventH\x00\x12*\n\x0chistoryState\x18\x13 \x01(\x0b\x32\x12.HistoryStateEventH\x00\x12,\n\rcontinueAsNew\x18\x14 \x01(\x0b\x32\x13.ContinueAsNewEventH\x00\x12\x36\n\x12\x65xecutionSuspended\x18\x15 \x01(\x0b\x32\x18.ExecutionSuspendedEventH\x00\x12\x32\n\x10\x65xecutionResumed\x18\x16 \x01(\x0b\x32\x16.ExecutionResumedEventH\x00\x42\x0b\n\teventType\"~\n\x12ScheduleTaskAction\x12\x0c\n\x04name\x18\x01 \x01(\t\x12-\n\x07version\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05input\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x9c\x01\n\x1c\x43reateSubOrchestrationAction\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12-\n\x07version\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05input\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"?\n\x11\x43reateTimerAction\x12*\n\x06\x66ireAt\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"u\n\x0fSendEventAction\x12(\n\x08instance\x18\x01 \x01(\x0b\x32\x16.OrchestrationInstance\x12\x0c\n\x04name\x18\x02 \x01(\t\x12*\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xb4\x02\n\x1b\x43ompleteOrchestrationAction\x12\x31\n\x13orchestrationStatus\x18\x01 \x01(\x0e\x32\x14.OrchestrationStatus\x12,\n\x06result\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\nnewVersion\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12&\n\x0f\x63\x61rryoverEvents\x18\x05 \x03(\x0b\x32\r.HistoryEvent\x12+\n\x0e\x66\x61ilureDetails\x18\x06 \x01(\x0b\x32\x13.TaskFailureDetails\"q\n\x1cTerminateOrchestrationAction\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12,\n\x06reason\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x0f\n\x07recurse\x18\x03 \x01(\x08\"\xfa\x02\n\x12OrchestratorAction\x12\n\n\x02id\x18\x01 \x01(\x05\x12+\n\x0cscheduleTask\x18\x02 \x01(\x0b\x32\x13.ScheduleTaskActionH\x00\x12?\n\x16\x63reateSubOrchestration\x18\x03 \x01(\x0b\x32\x1d.CreateSubOrchestrationActionH\x00\x12)\n\x0b\x63reateTimer\x18\x04 \x01(\x0b\x32\x12.CreateTimerActionH\x00\x12%\n\tsendEvent\x18\x05 \x01(\x0b\x32\x10.SendEventActionH\x00\x12=\n\x15\x63ompleteOrchestration\x18\x06 \x01(\x0b\x32\x1c.CompleteOrchestrationActionH\x00\x12?\n\x16terminateOrchestration\x18\x07 \x01(\x0b\x32\x1d.TerminateOrchestrationActionH\x00\x42\x18\n\x16orchestratorActionType\"\xda\x01\n\x13OrchestratorRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x31\n\x0b\x65xecutionId\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12!\n\npastEvents\x18\x03 \x03(\x0b\x32\r.HistoryEvent\x12 \n\tnewEvents\x18\x04 \x03(\x0b\x32\r.HistoryEvent\x12\x37\n\x10\x65ntityParameters\x18\x05 \x01(\x0b\x32\x1d.OrchestratorEntityParameters\"\x84\x01\n\x14OrchestratorResponse\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12$\n\x07\x61\x63tions\x18\x02 \x03(\x0b\x32\x13.OrchestratorAction\x12\x32\n\x0c\x63ustomStatus\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xd2\x01\n\x15\x43reateInstanceRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12-\n\x07version\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05input\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12;\n\x17scheduledStartTimestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\",\n\x16\x43reateInstanceResponse\x12\x12\n\ninstanceId\x18\x01 \x01(\t\"E\n\x12GetInstanceRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x1b\n\x13getInputsAndOutputs\x18\x02 \x01(\x08\"V\n\x13GetInstanceResponse\x12\x0e\n\x06\x65xists\x18\x01 \x01(\x08\x12/\n\x12orchestrationState\x18\x02 \x01(\x0b\x32\x13.OrchestrationState\"Y\n\x15RewindInstanceRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12,\n\x06reason\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x18\n\x16RewindInstanceResponse\"\x81\x04\n\x12OrchestrationState\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12-\n\x07version\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x13orchestrationStatus\x18\x04 \x01(\x0e\x32\x14.OrchestrationStatus\x12;\n\x17scheduledStartTimestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x10\x63reatedTimestamp\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x38\n\x14lastUpdatedTimestamp\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x05input\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06output\x18\t \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0c\x63ustomStatus\x18\n \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x0e\x66\x61ilureDetails\x18\x0b \x01(\x0b\x32\x13.TaskFailureDetails\"b\n\x11RaiseEventRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12+\n\x05input\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x14\n\x12RaiseEventResponse\"g\n\x10TerminateRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12,\n\x06output\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x11\n\trecursive\x18\x03 \x01(\x08\"\x13\n\x11TerminateResponse\"R\n\x0eSuspendRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12,\n\x06reason\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x11\n\x0fSuspendResponse\"Q\n\rResumeRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12,\n\x06reason\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x10\n\x0eResumeResponse\"6\n\x15QueryInstancesRequest\x12\x1d\n\x05query\x18\x01 \x01(\x0b\x32\x0e.InstanceQuery\"\x82\x03\n\rInstanceQuery\x12+\n\rruntimeStatus\x18\x01 \x03(\x0e\x32\x14.OrchestrationStatus\x12\x33\n\x0f\x63reatedTimeFrom\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rcreatedTimeTo\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x0ctaskHubNames\x18\x04 \x03(\x0b\x32\x1c.google.protobuf.StringValue\x12\x18\n\x10maxInstanceCount\x18\x05 \x01(\x05\x12\x37\n\x11\x63ontinuationToken\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10instanceIdPrefix\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x1d\n\x15\x66\x65tchInputsAndOutputs\x18\x08 \x01(\x08\"\x82\x01\n\x16QueryInstancesResponse\x12/\n\x12orchestrationState\x18\x01 \x03(\x0b\x32\x13.OrchestrationState\x12\x37\n\x11\x63ontinuationToken\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"m\n\x15PurgeInstancesRequest\x12\x14\n\ninstanceId\x18\x01 \x01(\tH\x00\x12\x33\n\x13purgeInstanceFilter\x18\x02 \x01(\x0b\x32\x14.PurgeInstanceFilterH\x00\x42\t\n\x07request\"\xaa\x01\n\x13PurgeInstanceFilter\x12\x33\n\x0f\x63reatedTimeFrom\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rcreatedTimeTo\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\rruntimeStatus\x18\x03 \x03(\x0e\x32\x14.OrchestrationStatus\"6\n\x16PurgeInstancesResponse\x12\x1c\n\x14\x64\x65letedInstanceCount\x18\x01 \x01(\x05\"0\n\x14\x43reateTaskHubRequest\x12\x18\n\x10recreateIfExists\x18\x01 \x01(\x08\"\x17\n\x15\x43reateTaskHubResponse\"\x16\n\x14\x44\x65leteTaskHubRequest\"\x17\n\x15\x44\x65leteTaskHubResponse\"\xaa\x01\n\x13SignalEntityRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12+\n\x05input\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x11\n\trequestId\x18\x04 \x01(\t\x12\x31\n\rscheduledTime\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x16\n\x14SignalEntityResponse\"<\n\x10GetEntityRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x14\n\x0cincludeState\x18\x02 \x01(\x08\"D\n\x11GetEntityResponse\x12\x0e\n\x06\x65xists\x18\x01 \x01(\x08\x12\x1f\n\x06\x65ntity\x18\x02 \x01(\x0b\x32\x0f.EntityMetadata\"\xcb\x02\n\x0b\x45ntityQuery\x12:\n\x14instanceIdStartsWith\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x10lastModifiedFrom\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x0elastModifiedTo\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x14\n\x0cincludeState\x18\x04 \x01(\x08\x12\x18\n\x10includeTransient\x18\x05 \x01(\x08\x12-\n\x08pageSize\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x37\n\x11\x63ontinuationToken\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"3\n\x14QueryEntitiesRequest\x12\x1b\n\x05query\x18\x01 \x01(\x0b\x32\x0c.EntityQuery\"s\n\x15QueryEntitiesResponse\x12!\n\x08\x65ntities\x18\x01 \x03(\x0b\x32\x0f.EntityMetadata\x12\x37\n\x11\x63ontinuationToken\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xdb\x01\n\x0e\x45ntityMetadata\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x34\n\x10lastModifiedTime\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x18\n\x10\x62\x61\x63klogQueueSize\x18\x03 \x01(\x05\x12.\n\x08lockedBy\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x0fserializedState\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x8f\x01\n\x19\x43leanEntityStorageRequest\x12\x37\n\x11\x63ontinuationToken\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x1b\n\x13removeEmptyEntities\x18\x02 \x01(\x08\x12\x1c\n\x14releaseOrphanedLocks\x18\x03 \x01(\x08\"\x92\x01\n\x1a\x43leanEntityStorageResponse\x12\x37\n\x11\x63ontinuationToken\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x1c\n\x14\x65mptyEntitiesRemoved\x18\x02 \x01(\x05\x12\x1d\n\x15orphanedLocksReleased\x18\x03 \x01(\x05\"]\n\x1cOrchestratorEntityParameters\x12=\n\x1a\x65ntityMessageReorderWindow\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\"\x82\x01\n\x12\x45ntityBatchRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x31\n\x0b\x65ntityState\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12%\n\noperations\x18\x03 \x03(\x0b\x32\x11.OperationRequest\"\xb9\x01\n\x11\x45ntityBatchResult\x12!\n\x07results\x18\x01 \x03(\x0b\x32\x10.OperationResult\x12!\n\x07\x61\x63tions\x18\x02 \x03(\x0b\x32\x10.OperationAction\x12\x31\n\x0b\x65ntityState\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x0e\x66\x61ilureDetails\x18\x04 \x01(\x0b\x32\x13.TaskFailureDetails\"e\n\x10OperationRequest\x12\x11\n\toperation\x18\x01 \x01(\t\x12\x11\n\trequestId\x18\x02 \x01(\t\x12+\n\x05input\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"w\n\x0fOperationResult\x12*\n\x07success\x18\x01 \x01(\x0b\x32\x17.OperationResultSuccessH\x00\x12*\n\x07\x66\x61ilure\x18\x02 \x01(\x0b\x32\x17.OperationResultFailureH\x00\x42\x0c\n\nresultType\"F\n\x16OperationResultSuccess\x12,\n\x06result\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"E\n\x16OperationResultFailure\x12+\n\x0e\x66\x61ilureDetails\x18\x01 \x01(\x0b\x32\x13.TaskFailureDetails\"\x9c\x01\n\x0fOperationAction\x12\n\n\x02id\x18\x01 \x01(\x05\x12\'\n\nsendSignal\x18\x02 \x01(\x0b\x32\x11.SendSignalActionH\x00\x12=\n\x15startNewOrchestration\x18\x03 \x01(\x0b\x32\x1c.StartNewOrchestrationActionH\x00\x42\x15\n\x13operationActionType\"\x94\x01\n\x10SendSignalAction\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12+\n\x05input\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\rscheduledTime\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xce\x01\n\x1bStartNewOrchestrationAction\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12-\n\x07version\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05input\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\rscheduledTime\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x15\n\x13GetWorkItemsRequest\"\xa5\x01\n\x08WorkItem\x12\x33\n\x13orchestratorRequest\x18\x01 \x01(\x0b\x32\x14.OrchestratorRequestH\x00\x12+\n\x0f\x61\x63tivityRequest\x18\x02 \x01(\x0b\x32\x10.ActivityRequestH\x00\x12,\n\rentityRequest\x18\x03 \x01(\x0b\x32\x13.EntityBatchRequestH\x00\x42\t\n\x07request\"\x16\n\x14\x43ompleteTaskResponse*\xb5\x02\n\x13OrchestrationStatus\x12 \n\x1cORCHESTRATION_STATUS_RUNNING\x10\x00\x12\"\n\x1eORCHESTRATION_STATUS_COMPLETED\x10\x01\x12)\n%ORCHESTRATION_STATUS_CONTINUED_AS_NEW\x10\x02\x12\x1f\n\x1bORCHESTRATION_STATUS_FAILED\x10\x03\x12!\n\x1dORCHESTRATION_STATUS_CANCELED\x10\x04\x12#\n\x1fORCHESTRATION_STATUS_TERMINATED\x10\x05\x12 \n\x1cORCHESTRATION_STATUS_PENDING\x10\x06\x12\"\n\x1eORCHESTRATION_STATUS_SUSPENDED\x10\x07\x32\xfc\n\n\x15TaskHubSidecarService\x12\x37\n\x05Hello\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\x12@\n\rStartInstance\x12\x16.CreateInstanceRequest\x1a\x17.CreateInstanceResponse\x12\x38\n\x0bGetInstance\x12\x13.GetInstanceRequest\x1a\x14.GetInstanceResponse\x12\x41\n\x0eRewindInstance\x12\x16.RewindInstanceRequest\x1a\x17.RewindInstanceResponse\x12\x41\n\x14WaitForInstanceStart\x12\x13.GetInstanceRequest\x1a\x14.GetInstanceResponse\x12\x46\n\x19WaitForInstanceCompletion\x12\x13.GetInstanceRequest\x1a\x14.GetInstanceResponse\x12\x35\n\nRaiseEvent\x12\x12.RaiseEventRequest\x1a\x13.RaiseEventResponse\x12:\n\x11TerminateInstance\x12\x11.TerminateRequest\x1a\x12.TerminateResponse\x12\x34\n\x0fSuspendInstance\x12\x0f.SuspendRequest\x1a\x10.SuspendResponse\x12\x31\n\x0eResumeInstance\x12\x0e.ResumeRequest\x1a\x0f.ResumeResponse\x12\x41\n\x0eQueryInstances\x12\x16.QueryInstancesRequest\x1a\x17.QueryInstancesResponse\x12\x41\n\x0ePurgeInstances\x12\x16.PurgeInstancesRequest\x1a\x17.PurgeInstancesResponse\x12\x31\n\x0cGetWorkItems\x12\x14.GetWorkItemsRequest\x1a\t.WorkItem0\x01\x12@\n\x14\x43ompleteActivityTask\x12\x11.ActivityResponse\x1a\x15.CompleteTaskResponse\x12H\n\x18\x43ompleteOrchestratorTask\x12\x15.OrchestratorResponse\x1a\x15.CompleteTaskResponse\x12?\n\x12\x43ompleteEntityTask\x12\x12.EntityBatchResult\x1a\x15.CompleteTaskResponse\x12>\n\rCreateTaskHub\x12\x15.CreateTaskHubRequest\x1a\x16.CreateTaskHubResponse\x12>\n\rDeleteTaskHub\x12\x15.DeleteTaskHubRequest\x1a\x16.DeleteTaskHubResponse\x12;\n\x0cSignalEntity\x12\x14.SignalEntityRequest\x1a\x15.SignalEntityResponse\x12\x32\n\tGetEntity\x12\x11.GetEntityRequest\x1a\x12.GetEntityResponse\x12>\n\rQueryEntities\x12\x15.QueryEntitiesRequest\x1a\x16.QueryEntitiesResponse\x12M\n\x12\x43leanEntityStorage\x12\x1a.CleanEntityStorageRequest\x1a\x1b.CleanEntityStorageResponseBf\n1com.microsoft.durabletask.implementation.protobufZ\x10/internal/protos\xaa\x02\x1eMicrosoft.DurableTask.Protobufb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'orchestrator_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n1com.microsoft.durabletask.implementation.protobufZ\020/internal/protos\252\002\036Microsoft.DurableTask.Protobuf'
  _TRACECONTEXT.fields_by_name['spanID']._options = None
  _TRACECONTEXT.fields_by_name['spanID']._serialized_options = b'\030\001'
  _ORCHESTRATIONSTATUS._serialized_start=11416
  _ORCHESTRATIONSTATUS._serialized_end=11725
  _ORCHESTRATIONINSTANCE._serialized_start=156
  _ORCHESTRATIONINSTANCE._serialized_end=250
  _ACTIVITYREQUEST._serialized_start=253
  _ACTIVITYREQUEST._serialized_end=447
  _ACTIVITYRESPONSE._serialized_start=450
  _ACTIVITYRESPONSE._serialized_end=595
  _TASKFAILUREDETAILS._serialized_start=598
  _TASKFAILUREDETAILS._serialized_end=776
  _PARENTINSTANCEINFO._serialized_start=779
  _PARENTINSTANCEINFO._serialized_end=970
  _TRACECONTEXT._serialized_start=972
  _TRACECONTEXT._serialized_end=1077
  _EXECUTIONSTARTEDEVENT._serialized_start=1080
  _EXECUTIONSTARTEDEVENT._serialized_end=1472
  _EXECUTIONCOMPLETEDEVENT._serialized_start=1475
  _EXECUTIONCOMPLETEDEVENT._serialized_end=1642
  _EXECUTIONTERMINATEDEVENT._serialized_start=1644
  _EXECUTIONTERMINATEDEVENT._serialized_end=1732
  _TASKSCHEDULEDEVENT._serialized_start=1735
  _TASKSCHEDULEDEVENT._serialized_end=1904
  _TASKCOMPLETEDEVENT._serialized_start=1906
  _TASKCOMPLETEDEVENT._serialized_end=1997
  _TASKFAILEDEVENT._serialized_start=1999
  _TASKFAILEDEVENT._serialized_end=2086
  _SUBORCHESTRATIONINSTANCECREATEDEVENT._serialized_start=2089
  _SUBORCHESTRATIONINSTANCECREATEDEVENT._serialized_end=2296
  _SUBORCHESTRATIONINSTANCECOMPLETEDEVENT._serialized_start=2298
  _SUBORCHESTRATIONINSTANCECOMPLETEDEVENT._serialized_end=2409
  _SUBORCHESTRATIONINSTANCEFAILEDEVENT._serialized_start=2411
  _SUBORCHESTRATIONINSTANCEFAILEDEVENT._serialized_end=2518
  _TIMERCREATEDEVENT._serialized_start=2520
  _TIMERCREATEDEVENT._serialized_end=2583
  _TIMERFIREDEVENT._serialized_start=2585
  _TIMERFIREDEVENT._serialized_end=2663
  _ORCHESTRATORSTARTEDEVENT._serialized_start=2665
  _ORCHESTRATORSTARTEDEVENT._serialized_end=2691
  _ORCHESTRATORCOMPLETEDEVENT._serialized_start=2693
  _ORCHESTRATORCOMPLETEDEVENT._serialized_end=2721
  _EVENTSENTEVENT._serialized_start=2723
  _EVENTSENTEVENT._serialized_end=2818
  _EVENTRAISEDEVENT._serialized_start=2820
  _EVENTRAISEDEVENT._serialized_end=2897
  _GENERICEVENT._serialized_start=2899
  _GENERICEVENT._serialized_end=2927
  _HISTORYSTATEEVENT._serialized_start=2929
  _HISTORYSTATEEVENT._serialized_end=2997
  _CONTINUEASNEWEVENT._serialized_start=2999
  _CONTINUEASNEWEVENT._serialized_end=3064
  _EXECUTIONSUSPENDEDEVENT._serialized_start=3066
  _EXECUTIONSUSPENDEDEVENT._serialized_end=3136
  _EXECUTIONRESUMEDEVENT._serialized_start=3138
  _EXECUTIONRESUMEDEVENT._serialized_end=3206
  _HISTORYEVENT._serialized_start=3209
  _HISTORYEVENT._serialized_end=4367
  _SCHEDULETASKACTION._serialized_start=4369
  _SCHEDULETASKACTION._serialized_end=4495
  _CREATESUBORCHESTRATIONACTION._serialized_start=4498
  _CREATESUBORCHESTRATIONACTION._serialized_end=4654
  _CREATETIMERACTION._serialized_start=4656
  _CREATETIMERACTION._serialized_end=4719
  _SENDEVENTACTION._serialized_start=4721
  _SENDEVENTACTION._serialized_end=4838
  _COMPLETEORCHESTRATIONACTION._serialized_start=4841
  _COMPLETEORCHESTRATIONACTION._serialized_end=5149
  _TERMINATEORCHESTRATIONACTION._serialized_start=5151
  _TERMINATEORCHESTRATIONACTION._serialized_end=5264
  _ORCHESTRATORACTION._serialized_start=5267
  _ORCHESTRATORACTION._serialized_end=5645
  _ORCHESTRATORREQUEST._serialized_start=5648
  _ORCHESTRATORREQUEST._serialized_end=5866
  _ORCHESTRATORRESPONSE._serialized_start=5869
  _ORCHESTRATORRESPONSE._serialized_end=6001
  _CREATEINSTANCEREQUEST._serialized_start=6004
  _CREATEINSTANCEREQUEST._serialized_end=6214
  _CREATEINSTANCERESPONSE._serialized_start=6216
  _CREATEINSTANCERESPONSE._serialized_end=6260
  _GETINSTANCEREQUEST._serialized_start=6262
  _GETINSTANCEREQUEST._serialized_end=6331
  _GETINSTANCERESPONSE._serialized_start=6333
  _GETINSTANCERESPONSE._serialized_end=6419
  _REWINDINSTANCEREQUEST._serialized_start=6421
  _REWINDINSTANCEREQUEST._serialized_end=6510
  _REWINDINSTANCERESPONSE._serialized_start=6512
  _REWINDINSTANCERESPONSE._serialized_end=6536
  _ORCHESTRATIONSTATE._serialized_start=6539
  _ORCHESTRATIONSTATE._serialized_end=7052
  _RAISEEVENTREQUEST._serialized_start=7054
  _RAISEEVENTREQUEST._serialized_end=7152
  _RAISEEVENTRESPONSE._serialized_start=7154
  _RAISEEVENTRESPONSE._serialized_end=7174
  _TERMINATEREQUEST._serialized_start=7176
  _TERMINATEREQUEST._serialized_end=7279
  _TERMINATERESPONSE._serialized_start=7281
  _TERMINATERESPONSE._serialized_end=7300
  _SUSPENDREQUEST._serialized_start=7302
  _SUSPENDREQUEST._serialized_end=7384
  _SUSPENDRESPONSE._serialized_start=7386
  _SUSPENDRESPONSE._serialized_end=7403
  _RESUMEREQUEST._serialized_start=7405
  _RESUMEREQUEST._serialized_end=7486
  _RESUMERESPONSE._serialized_start=7488
  _RESUMERESPONSE._serialized_end=7504
  _QUERYINSTANCESREQUEST._serialized_start=7506
  _QUERYINSTANCESREQUEST._serialized_end=7560
  _INSTANCEQUERY._serialized_start=7563
  _INSTANCEQUERY._serialized_end=7949
  _QUERYINSTANCESRESPONSE._serialized_start=7952
  _QUERYINSTANCESRESPONSE._serialized_end=8082
  _PURGEINSTANCESREQUEST._serialized_start=8084
  _PURGEINSTANCESREQUEST._serialized_end=8193
  _PURGEINSTANCEFILTER._serialized_start=8196
  _PURGEINSTANCEFILTER._serialized_end=8366
  _PURGEINSTANCESRESPONSE._serialized_start=8368
  _PURGEINSTANCESRESPONSE._serialized_end=8422
  _CREATETASKHUBREQUEST._serialized_start=8424
  _CREATETASKHUBREQUEST._serialized_end=8472
  _CREATETASKHUBRESPONSE._serialized_start=8474
  _CREATETASKHUBRESPONSE._serialized_end=8497
  _DELETETASKHUBREQUEST._serialized_start=8499
  _DELETETASKHUBREQUEST._serialized_end=8521
  _DELETETASKHUBRESPONSE._serialized_start=8523
  _DELETETASKHUBRESPONSE._serialized_end=8546
  _SIGNALENTITYREQUEST._serialized_start=8549
  _SIGNALENTITYREQUEST._serialized_end=8719
  _SIGNALENTITYRESPONSE._serialized_start=8721
  _SIGNALENTITYRESPONSE._serialized_end=8743
  _GETENTITYREQUEST._serialized_start=8745
  _GETENTITYREQUEST._serialized_end=8805
  _GETENTITYRESPONSE._serialized_start=8807
  _GETENTITYRESPONSE._serialized_end=8875
  _ENTITYQUERY._serialized_start=8878
  _ENTITYQUERY._serialized_end=9209
  _QUERYENTITIESREQUEST._serialized_start=9211
  _QUERYENTITIESREQUEST._serialized_end=9262
  _QUERYENTITIESRESPONSE._serialized_start=9264
  _QUERYENTITIESRESPONSE._serialized_end=9379
  _ENTITYMETADATA._serialized_start=9382
  _ENTITYMETADATA._serialized_end=9601
  _CLEANENTITYSTORAGEREQUEST._serialized_start=9604
  _CLEANENTITYSTORAGEREQUEST._serialized_end=9747
  _CLEANENTITYSTORAGERESPONSE._serialized_start=9750
  _CLEANENTITYSTORAGERESPONSE._serialized_end=9896
  _ORCHESTRATORENTITYPARAMETERS._serialized_start=9898
  _ORCHESTRATORENTITYPARAMETERS._serialized_end=9991
  _ENTITYBATCHREQUEST._serialized_start=9994
  _ENTITYBATCHREQUEST._serialized_end=10124
  _ENTITYBATCHRESULT._serialized_start=10127
  _ENTITYBATCHRESULT._serialized_end=10312
  _OPERATIONREQUEST._serialized_start=10314
  _OPERATIONREQUEST._serialized_end=10415
  _OPERATIONRESULT._serialized_start=10417
  _OPERATIONRESULT._serialized_end=10536
  _OPERATIONRESULTSUCCESS._serialized_start=10538
  _OPERATIONRESULTSUCCESS._serialized_end=10608
  _OPERATIONRESULTFAILURE._serialized_start=10610
  _OPERATIONRESULTFAILURE._serialized_end=10679
  _OPERATIONACTION._serialized_start=10682
  _OPERATIONACTION._serialized_end=10838
  _SENDSIGNALACTION._serialized_start=10841
  _SENDSIGNALACTION._serialized_end=10989
  _STARTNEWORCHESTRATIONACTION._serialized_start=10992
  _STARTNEWORCHESTRATIONACTION._serialized_end=11198
  _GETWORKITEMSREQUEST._serialized_start=11200
  _GETWORKITEMSREQUEST._serialized_end=11221
  _WORKITEM._serialized_start=11224
  _WORKITEM._serialized_end=11389
  _COMPLETETASKRESPONSE._serialized_start=11391
  _COMPLETETASKRESPONSE._serialized_end=11413
  _TASKHUBSIDECARSERVICE._serialized_start=11728
  _TASKHUBSIDECARSERVICE._serialized_end=13132
# @@protoc_insertion_point(module_scope)
