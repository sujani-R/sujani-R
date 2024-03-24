package day8;

import static io.restassured.RestAssured.*;
import static io.restassured.matcher.RestAssuredMatchers.*;
import static org.hamcrest.Matchers.*;

import org.json.JSONObject;
import org.testng.ITestContext;
import org.testng.annotations.Test;

import io.restassured.response.Response;
//as the 4 tests are linked via an id a testng xml file is needed to run these tests

public class getuser {
	@Test
	void test_getuser(ITestContext context)
	{
		String bearerToken=" add token from postman";
		//int id=(Integer)context.getAttribute("user_id");
		int id=(Integer)context.getSuite().getAttribute("user_id"); //to run the tests indivisually
		
		int id= given()
			.headers("Authorizations","Bearer "+bearerToken);
			.Pathparam("id", id)
		
		when()
			.get("incomplete URL/{id}");		
		
		then()
			.statusCode(200);
			.log().all();
			
		
		
	}

}
