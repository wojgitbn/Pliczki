curl -X POST http://10.3.6.31:9082/WS14_414_040G/services/wapiOtherSoapHttpPort ^
  -H "Content-Type: text/xml; charset=UTF-8" ^
  -H "SOAPAction: http://wapiOther/WapiOther.wsdl/getserviceinfoother" ^
  -H "instanceNo: 95460004" ^
  -H "Accept-Encoding: gzip,deflate" ^
  -H "Connection: Keep-Alive" ^
  -H "User-Agent: Apache-HttpClient/4.5.5 (Java/16.0.2)" ^
  --data @soap_request.xml
pause