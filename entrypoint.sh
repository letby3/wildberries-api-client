ROOT_DIR_PWD="`pwd`"
SWAGGER_FILE_DIR="`pwd`/wildberries_api_client/_swagger_doc"
SWAGGER_OUTPUT="`pwd`/wildberries_api_client"

wget -O "$SWAGGER_FILE_DIR/swagger_promotion.yaml" \
  https://openapi.wildberries.ru/promotion/swagger/api/ru/swagger.yaml \
  -T5 \
  --no-check-certificate \
  --retry-connrefused --waitretry=10 --read-timeout=20 --timeout=15 -t 0

wget -O "$SWAGGER_FILE_DIR/swagger_content.yaml" \
  https://openapi.wildberries.ru/content/swagger/api/ru/swagger.yaml \
  -T5 \
  --no-check-certificate \
  --retry-connrefused --waitretry=10 --read-timeout=20 --timeout=15 -t 0

wget -O "$SWAGGER_FILE_DIR/swagger_prices.yaml" \
  https://openapi.wildberries.ru/prices/swagger/api/ru/swagger.yaml \
  -T5 \
  --no-check-certificate \
  --retry-connrefused --waitretry=10 --read-timeout=20 --timeout=15 -t 0

wget -O "$SWAGGER_FILE_DIR/swagger_marketplace.yaml" \
  https://openapi.wildberries.ru/marketplace/swagger/api/ru/swagger.yaml \
  -T5 \
  --no-check-certificate \
  --retry-connrefused --waitretry=10 --read-timeout=20 --timeout=15 -t 0

wget -O "$SWAGGER_FILE_DIR/swagger_statistics.yaml" \
  https://openapi.wildberries.ru/statistics/swagger/api/ru/swagger.yaml \
  -T5 \
  --no-check-certificate \
  --retry-connrefused --waitretry=10 --read-timeout=20 --timeout=15 -t 0

wget -O "$SWAGGER_FILE_DIR/swagger_analytics.yaml" \
  https://openapi.wildberries.ru/analytics/swagger/api/ru/swagger.yaml \
  -T5 \
  --no-check-certificate \
  --retry-connrefused --waitretry=10 --read-timeout=20 --timeout=15 -t 0

wget -O "$SWAGGER_FILE_DIR/swagger_recommendations.yaml" \
  https://openapi.wildberries.ru/recommendations/swagger/api/ru/swagger.yaml \
  -T5 \
  --no-check-certificate \
  --retry-connrefused --waitretry=10 --read-timeout=20 --timeout=15 -t 0

wget -O "$SWAGGER_FILE_DIR/swagger_feedbacks_questions.yaml" \
  https://openapi.wildberries.ru/feedbacks-questions/swagger/api/ru/swagger.yaml \
  -T5 \
  --no-check-certificate \
  --retry-connrefused --waitretry=10 --read-timeout=20 --timeout=15 -t 0

wget -O "$SWAGGER_FILE_DIR/swagger_tariffs.yaml" \
  https://openapi.wildberries.ru/tariffs/swagger/api/ru/swagger.yaml \
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
    -i "$SWAGGER_FILE_DIR/swagger_promotion.yaml" \
    -l python \
    -o "$SWAGGER_OUTPUT/promotion_pred" \
    --additional-properties packageName=wildberries_api_client.promotion

java -jar swagger-codegen-cli.jar generate \
    -i "$SWAGGER_FILE_DIR/swagger_content.yaml" \
    -l python \
    -o "$SWAGGER_OUTPUT/content_pred" \
    --additional-properties packageName=wildberries_api_client.content

java -jar swagger-codegen-cli.jar generate \
    -i "$SWAGGER_FILE_DIR/swagger_prices.yaml" \
    -l python \
    -o "$SWAGGER_OUTPUT/prices_pred" \
    --additional-properties packageName=wildberries_api_client.prices

java -jar swagger-codegen-cli.jar generate \
    -i "$SWAGGER_FILE_DIR/swagger_marketplace.yaml" \
    -l python \
    -o "$SWAGGER_OUTPUT/marketplace_pred" \
    --additional-properties packageName=wildberries_api_client.marketplace

java -jar swagger-codegen-cli.jar generate \
    -i "$SWAGGER_FILE_DIR/swagger_statistics.yaml" \
    -l python \
    -o "$SWAGGER_OUTPUT/statistics_pred" \
    --additional-properties packageName=wildberries_api_client.statistics

java -jar swagger-codegen-cli.jar generate \
    -i "$SWAGGER_FILE_DIR/swagger_analytics.yaml" \
    -l python \
    -o "$SWAGGER_OUTPUT/analytics_pred" \
    --additional-properties packageName=wildberries_api_client.analytics

java -jar swagger-codegen-cli.jar generate \
    -i "$SWAGGER_FILE_DIR/swagger_recommendations.yaml" \
    -l python \
    -o "$SWAGGER_OUTPUT/recommendations_pred" \
    --additional-properties packageName=wildberries_api_client.recommendations

java -jar swagger-codegen-cli.jar generate \
    -i "$SWAGGER_FILE_DIR/swagger_feedbacks_questions.yaml" \
    -l python \
    -o "$SWAGGER_OUTPUT/feedbacks_questions_pred" \
    --additional-properties packageName=wildberries_api_client.feedbacks_questions

java -jar swagger-codegen-cli.jar generate \
    -i "$SWAGGER_FILE_DIR/swagger_tariffs.yaml" \
    -l python \
    -o "$SWAGGER_OUTPUT/tariffs_pred" \
    --additional-properties packageName=wildberries_api_client.tariffs

cd $SWAGGER_OUTPUT

mv ./promotion_pred/wildberries_api_client/promotion ./
rm -rf ./promotion_pred

mv ./content_pred/wildberries_api_client/content ./
rm -rf ./content_pred

mv ./prices_pred/wildberries_api_client/prices ./
rm -rf ./prices_pred

mv ./marketplace_pred/wildberries_api_client/marketplace ./
rm -rf ./marketplace_pred

mv ./statistics_pred/wildberries_api_client/statistics ./
rm -rf ./statistics_pred

mv ./analytics_pred/wildberries_api_client/analytics ./
rm -rf ./analytics_pred

mv ./recommendations_pred/wildberries_api_client/recommendations ./
rm -rf ./recommendations_pred

mv ./feedbacks_questions_pred/wildberries_api_client/feedbacks_questions ./
rm -rf ./feedbacks_questions_pred

mv ./tariffs_pred/wildberries_api_client/tariffs ./
rm -rf ./tariffs_pred

