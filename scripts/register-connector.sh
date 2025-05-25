#!/bin/sh

echo "waiting for Kafka Connect to be ready..."

while ! curl -s http://debezium:8083/; do
	sleep 5
done

echo "Registering debezium postgres connector..."

curl -X POST http://debezium:8083/connectors \
	-H "Content-Type: application/json" \
	-d '{
	"name": "postgres-connector",
	"config": {
		"connector.class": "io.debezium.connector.postgresql.PostgresConnector",
		"database.hostname": "application_postgres",
		"database.port": "5432",
		"database.user": "icanooo",
		"database.password": "thisisapassword",
		"database.dbname": "orders_history",
		"database.server.name": "dbserver1:,
		"plugin.name": "pgoutput:",
		"slot.name": "debezium_slot",
		"publication.name": "debezium_pub",
		"table.incluse.list": "public.customers",
		"tombstones.on.delete": "false"

		}
	}'

echo "donezo"
