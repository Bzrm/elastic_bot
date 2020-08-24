from elasticsearch import Elasticsearch

#es=Elasticsearch()
#es.indices.delete(index="japanese")
#es.indices.delete(index="korean")
#es.indices.delete(index="russian")

#es.indices.create(index="japanese")
#es.indices.create(index="korean")
#es.indices.create(index="russian")

mapit_jap = {

    "msg": {
        "properties": {"msg_date": {"type": "date", "format": "YYYY-MM-DD"},
                                    "msg_time": {"type": "date", "format": "HH:mm"},
                                    "msg_datetime": {"type": "date", "format": "YYYY-MM-DD HH:mm"},
                                    "sender": {"type": "text", "analyzer": "keyword"},
                                    "chat_id": {"type": "text", "analyzer": "keyword"},
                                    "msg": {"type": "text", "analyzer": "standard"},
                                    "tokenized_msg": {"type": "text", "analyzer": "standard"
                                                      }}}}

mapit_kor = {

    "msg": {
        "properties": {"msg_date": {"type": "date", "format": "YYYY-MM-DD"},
                                    "msg_time": {"type": "date", "format": "HH:mm"},
                                    "msg_datetime": {"type": "date", "format": "YYYY-MM-DD HH:mm"},
                                    "sender": {"type": "text", "analyzer": "keyword"},
                                    "chat_id": {"type": "text", "analyzer": "keyword"},
                                    "msg": {"type": "text", "analyzer": "korean"},
                                    "tokenized_msg": {"type": "text", "analyzer": "korean"
                                                      }}}}

mapit_ru = {

    "msg": {
        "properties": {"msg_date": {"type": "date", "format": "YYYY-MM-DD"},
                                    "msg_time": {"type": "date", "format": "HH:mm"},
                                    "msg_datetime": {"type": "date", "format": "YYYY-MM-DD HH:mm"},
                                    "sender": {"type": "text", "analyzer": "keyword"},
                                    "chat_id": {"type": "text", "analyzer": "keyword"},
                                    "msg": {"type": "text", "analyzer": "russian"},
                                    "tokenized_msg": {"type": "text", "analyzer": "russian"
                                                      }}}}

#es.indices.put_mapping(index='japanese', doc_type='msg', body=mapit_jap, include_type_name=True)
#es.indices.put_mapping(index='korean', doc_type='msg', body=mapit_jap, include_type_name=True)
#es.indices.put_mapping(index='russian', doc_type='msg', body=mapit_jap, include_type_name=True)

