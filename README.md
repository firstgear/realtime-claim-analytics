
# Realtime insurance claim analytics

## Description

This project aims to build a realtime insurance usecase where insurance claims are processed through the use of realtime analytics. A couple of components:
- producer - streams realtime insurance claim events to a kafka topic
- kafka - kafka is used as intermediary between claim creation and claim processing
- spark - TOBE spark structured streaming to ingest these events and provide realtime anaytics


## Deployment

```
$ git clone ...
$ sudo docker-compose up
[+] Running 2/2
 ✔ Container kafka     Recreated                                                                                                                                                      0.1s 
 ✔ Container producer  Recreated                  
...
kafka     | [2024-07-23 13:55:17,483] INFO [KafkaRaftServer nodeId=1] Kafka Server started (kafka.server.KafkaRaftServer)
...
producer  | INFO:root:Sent: {'timestamp': '2024-07-23T13:55:28.518322', 'claim_type': 'car', 'fraud_score': 79, 'claim_value': 2747}
producer  | INFO:root:Sent: {'timestamp': '2024-07-23T13:55:29.520408', 'claim_type': 'car', 'fraud_score': 32, 'claim_value': 7783}
producer  | INFO:root:Sent: {'timestamp': '2024-07-23T13:55:30.522376', 'claim_type': 'car', 'fraud_score': 47, 'claim_value': 3495}
producer  | INFO:root:Sent: {'timestamp': '2024-07-23T13:55:31.525346', 'claim_type': 'car', 'fraud_score': 23, 'claim_value': 4007}
producer  | INFO:root:Sent: {'timestamp': '2024-07-23T13:55:32.527398', 'claim_type': 'car', 'fraud_score': 6, 'claim_value': 4294}
...
```

