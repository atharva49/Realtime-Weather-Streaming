from kafka.admin import KafkaAdminClient, NewTopic

def create_kafka_topic(topic_name, num_partitions=1, replication_factor=1):
    admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092")

    topic_list = [NewTopic(name=topic_name,num_partitions= num_partitions, replication_factor=replication_factor)]
    admin_client.create_topics(new_topics=topic_list,validate_only=False)
    print(f"Topic '{topic_name}' created successfully")


if __name__ == '__main__':
    topics = ["weather_data", "humidity_data", "temperature_data", "wind_speed_data", "pressure_data"]
    for topic in topics:
        create_kafka_topic(topic)