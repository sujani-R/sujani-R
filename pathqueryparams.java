package day3;

import static io.restassured.RestAssured.*;
import static io.restassured.matcher.RestAssuredMatchers.*;
import static org.hamcrest.Matchers.*;

import org.testng.annotations.Test;

public class pathqueryparams 
{	
	@Test
	void testqueryandpathparams()
	{
		given()
			.queryParam("mypath","users") //path params
			.queryParam("page","2")//query param
			.queryParam("id","5")//query partam
		
		.when()
			.get("https://reqres.in/api/(mypath)")//do not add query params
		
		.then()
			.statusCode(200)
			.log().all();
		
	}
}
