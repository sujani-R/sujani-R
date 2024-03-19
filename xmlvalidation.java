package day5;

import static io.restassured.RestAssured.*;
import static io.restassured.matcher.RestAssuredMatchers.*;
import static org.hamcrest.Matchers.*;

import java.util.List;

import org.testng.Assert;

import io.restassured.path.xml.XmlPath;
import io.restassured.response.Response;

public class xmlvalidation {

	void testxmlResponse()
	{
		//approach1
		/*given()
		
		.when()
			.get("http://restapi.adequateshop.com/api/Traveler?page=1")
		
		.then()
			.statusCode(200)
			.header("Content-Type","applicatrion/xml: charset=utf-8")
			.body("TravelinformationResponse.page", equalTo("1"))
			.body("TravelinformationResponse.travelers.Travelerinformation[0].name", equalTo("Vijay Bharath Reddy"));*/
		
		//approach2
		Response res= given()
		
		.when()
			.get("http://restapi.adequateshop.com/api/Traveler?page=1");
			
		Assert.assertEquals(res.getStatusCode(),200);
		Assert.assertEquals(res.header("Content-Type"),"applicatrion/xml: charset=utf-8");
		String pageno= res.xmlPath().get("TravelinformationResponse.page").toString();
		Assert.assertEquals(pageno,"1");
		
		String name= res.xmlPath().get("TravelinformationResponse.travelers.Travelerinformation[0].name").toString();
		Assert.assertEquals(name,"Vijay Bharath Reddy");
		
		
		
	}
	void testxmlResponsebody()
	{
		Response res= given()
		
		.when()
			.get("http://restapi.adequateshop.com/api/Traveler?page=1");
		
		//finding no of travelers		
		XmlPath xmlobj =  new XmlPath(res.asString());
		List<String> travelers= xmlobj.getList("TravelinformationResponse.Traveler.Travelinformation");
		Assert.assertEquals(travelers.size(),10);
		
		//verify a particular name
		List<String> traveler_names= xmlobj.getList("TravelinformationResponse.Traveler.Travelinformation.name");
		for (String traveler_name:traveler_names )	
		{
			if (traveler_name.equals("vijay bharath reddy"))
				{
				break;
		        }
		}
		
	}

}
