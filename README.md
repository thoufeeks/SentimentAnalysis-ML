# It a ML operationl Project for Sentiment Analysis
--------------------------------------------------
User POSTs JSON with text:


{ "text": "I really love this product!" }

✅ Response:

{ "prediction": "positive" }


---------
test

----
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "I love this tool!"}'
