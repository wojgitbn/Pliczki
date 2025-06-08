curl -X POST http://10.3.6.31:9082/WS14_414_040G/services/wapiOtherSoapHttpPort ^
  -H "Content-Type: text/xml; charset=UTF-8" ^
  -H "SOAPAction: http://wapiOther/WapiOther.wsdl/getserviceinfoother" ^
  -H "instanceNo: 95460004" ^
  --data @soap_request.xml
pause