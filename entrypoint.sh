ROOT_DIR_PWD="`pwd`"
SWAGGER_FILE_DIR="`pwd`/wildberries_api_client/_swagger_doc"
SWAGGER_OUTPUT="`pwd`/wildberries_api_client"

rm -rf $SWAGGER_OUTPUT/products/*
rm -rf $SWAGGER_OUTPUT/orders_fbs/*
rm -rf $SWAGGER_OUTPUT/orders_dbs/*
rm -rf $SWAGGER_OUTPUT/pickup/*
rm -rf $SWAGGER_OUTPUT/orders_fbw/*
rm -rf $SWAGGER_OUTPUT/promotion/*
rm -rf $SWAGGER_OUTPUT/communications/*
rm -rf $SWAGGER_OUTPUT/tariffs/*
rm -rf $SWAGGER_OUTPUT/analytics/*
rm -rf $SWAGGER_OUTPUT/reports/*
rm -rf $SWAGGER_OUTPUT/finances/*
rm -rf $SWAGGER_OUTPUT/wbd/*

wget -O "$SWAGGER_FILE_DIR/swagger_products.yaml" \
  https://dev.wildberries.ru/yaml/ru/02-products.yaml \
  -T5 \
  --no-check-certificate \
  --retry-connrefused --waitretry=10 --read-timeout=20 --timeout=15 -t 0

wget -O "$SWAGGER_FILE_DIR/swagger_orders_fbs.yaml" \
  https://dev.wildberries.ru/yaml/ru/03-orders-fbs.yaml \
  -T5 \
  --no-check-certificate \
  --retry-connrefused --waitretry=10 --read-timeout=20 --timeout=15 -t 0

wget -O "$SWAGGER_FILE_DIR/swagger_orders_dbs.yaml" \
  https://dev.wildberries.ru/yaml/ru/04-orders-dbs.yaml \
  -T5 \
  --no-check-certificate \
  --retry-connrefused --waitretry=10 --read-timeout=20 --timeout=15 -t 0

wget -O "$SWAGGER_FILE_DIR/swagger_pickup.yaml" \
  https://dev.wildberries.ru/yaml/ru/05-in-store-pickup.yaml \
  -T5 \
  --no-check-certificate \
  --retry-connrefused --waitretry=10 --read-timeout=20 --timeout=15 -t 0

wget -O "$SWAGGER_FILE_DIR/swagger_orders_fbw.yaml" \
  https://dev.wildberries.ru/yaml/ru/06-orders-fbw.yaml \
  -T5 \
  --no-check-certificate \
  --retry-connrefused --waitretry=10 --read-timeout=20 --timeout=15 -t 0

wget -O "$SWAGGER_FILE_DIR/swagger_promotion.yaml" \
  https://dev.wildberries.ru/yaml/ru/07-promotion.yaml \
  -T5 \
  --no-check-certificate \
  --retry-connrefused --waitretry=10 --read-timeout=20 --timeout=15 -t 0

wget -O "$SWAGGER_FILE_DIR/swagger_communications.yaml" \
  https://dev.wildberries.ru/yaml/ru/08-communications.yaml \
  -T5 \
  --no-check-certificate \
  --retry-connrefused --waitretry=10 --read-timeout=20 --timeout=15 -t 0

wget -O "$SWAGGER_FILE_DIR/swagger_tariffs.yaml" \
  https://dev.wildberries.ru/yaml/ru/09-tariffs.yaml \
  -T5 \
  --no-check-certificate \
  --retry-connrefused --waitretry=10 --read-timeout=20 --timeout=15 -t 0

wget -O "$SWAGGER_FILE_DIR/swagger_analytics.yaml" \
  https://dev.wildberries.ru/yaml/ru/10-analytics.yaml \
  -T5 \
  --no-check-certificate \
  --retry-connrefused --waitretry=10 --read-timeout=20 --timeout=15 -t 0

wget -O "$SWAGGER_FILE_DIR/swagger_reports.yaml" \
  https://dev.wildberries.ru/yaml/ru/11-reports.yaml \
  -T5 \
  --no-check-certificate \
  --retry-connrefused --waitretry=10 --read-timeout=20 --timeout=15 -t 0

wget -O "$SWAGGER_FILE_DIR/swagger_finances.yaml" \
  https://dev.wildberries.ru/yaml/ru/12-finances.yaml \
  -T5 \
  --no-check-certificate \
  --retry-connrefused --waitretry=10 --read-timeout=20 --timeout=15 -t 0

wget -O "$SWAGGER_FILE_DIR/swagger_wbd.yaml" \
  https://dev.wildberries.ru/yaml/ru/13-wbd.yaml \
  -T5 \
  --no-check-certificate \
  --retry-connrefused --waitretry=10 --read-timeout=20 --timeout=15 -t 0

cd "$SWAGGER_FILE_DIR"
python3 transliterate_script.py
cd "$ROOT_DIR_PWD"
git clone https://github.com/swagger-api/swagger-codegen
cd swagger-codegen
git checkout v3.0.30

mvn clean package

cd ./modules/swagger-codegen-cli/target


java -jar swagger-codegen-cli.jar generate \
    -i "$SWAGGER_FILE_DIR/swagger_products.yaml" \
    -l python \
    -o "$SWAGGER_OUTPUT/products_pred" \
    --additional-properties packageName=wildberries_api_client.products

java -jar swagger-codegen-cli.jar generate \
    -i "$SWAGGER_FILE_DIR/swagger_orders_fbs.yaml" \
    -l python \
    -o "$SWAGGER_OUTPUT/orders_fbs_pred" \
    --additional-properties packageName=wildberries_api_client.orders_fbs

java -jar swagger-codegen-cli.jar generate \
    -i "$SWAGGER_FILE_DIR/swagger_orders_dbs.yaml" \
    -l python \
    -o "$SWAGGER_OUTPUT/orders_dbs_pred" \
    --additional-properties packageName=wildberries_api_client.orders_dbs

java -jar swagger-codegen-cli.jar generate \
    -i "$SWAGGER_FILE_DIR/swagger_pickup.yaml" \
    -l python \
    -o "$SWAGGER_OUTPUT/pickup_pred" \
    --additional-properties packageName=wildberries_api_client.pickup

java -jar swagger-codegen-cli.jar generate \
    -i "$SWAGGER_FILE_DIR/swagger_orders_fbw.yaml" \
    -l python \
    -o "$SWAGGER_OUTPUT/orders_fbw_pred" \
    --additional-properties packageName=wildberries_api_client.orders_fbw

java -jar swagger-codegen-cli.jar generate \
    -i "$SWAGGER_FILE_DIR/swagger_promotion.yaml" \
    -l python \
    -o "$SWAGGER_OUTPUT/promotion_pred" \
    --additional-properties packageName=wildberries_api_client.promotion

java -jar swagger-codegen-cli.jar generate \
    -i "$SWAGGER_FILE_DIR/swagger_communications.yaml" \
    -l python \
    -o "$SWAGGER_OUTPUT/communications_pred" \
    --additional-properties packageName=wildberries_api_client.communications

java -jar swagger-codegen-cli.jar generate \
    -i "$SWAGGER_FILE_DIR/swagger_tariffs.yaml" \
    -l python \
    -o "$SWAGGER_OUTPUT/tariffs_pred" \
    --additional-properties packageName=wildberries_api_client.tariffs

java -jar swagger-codegen-cli.jar generate \
    -i "$SWAGGER_FILE_DIR/swagger_analytics.yaml" \
    -l python \
    -o "$SWAGGER_OUTPUT/analytics_pred" \
    --additional-properties packageName=wildberries_api_client.analytics

java -jar swagger-codegen-cli.jar generate \
    -i "$SWAGGER_FILE_DIR/swagger_reports.yaml" \
    -l python \
    -o "$SWAGGER_OUTPUT/reports_pred" \
    --additional-properties packageName=wildberries_api_client.reports

java -jar swagger-codegen-cli.jar generate \
    -i "$SWAGGER_FILE_DIR/swagger_finances.yaml" \
    -l python \
    -o "$SWAGGER_OUTPUT/finances_pred" \
    --additional-properties packageName=wildberries_api_client.finances

java -jar swagger-codegen-cli.jar generate \
    -i "$SWAGGER_FILE_DIR/swagger_wbd.yaml" \
    -l python \
    -o "$SWAGGER_OUTPUT/wbd_pred" \
    --additional-properties packageName=wildberries_api_client.wbd

cd $SWAGGER_OUTPUT

mv ./products_pred/wildberries_api_client/products ./
rm -rf ./products_pred

mv ./orders_fbs_pred/wildberries_api_client/orders_fbs ./
rm -rf ./orders_fbs_pred

mv ./orders_dbs_pred/wildberries_api_client/orders_dbs ./
rm -rf ./orders_dbs_pred

mv ./pickup_pred/wildberries_api_client/pickup ./
rm -rf ./pickup_pred

mv ./orders_fbw_pred/wildberries_api_client/orders_fbw ./
rm -rf ./orders_fbw_pred

mv ./promotion_pred/wildberries_api_client/promotion ./
rm -rf ./promotion_pred

mv ./communications_pred/wildberries_api_client/communications ./
rm -rf ./communications_pred

mv ./tariffs_pred/wildberries_api_client/tariffs ./
rm -rf ./tariffs_pred

mv ./analytics_pred/wildberries_api_client/analytics ./
rm -rf ./analytics_pred

mv ./reports_pred/wildberries_api_client/reports ./
rm -rf ./reports_pred

mv ./finances_pred/wildberries_api_client/finances ./
rm -rf ./finances_pred

mv ./wbd_pred/wildberries_api_client/wbd ./
rm -rf ./wbd_pred

