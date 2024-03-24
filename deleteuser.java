package day8;

import static io.restassured.RestAssured.*;
import static io.restassured.matcher.RestAssuredMatchers.*;
import static org.hamcrest.Matchers.*;

import org.json.JSONObject;
import org.testng.ITestContext;
import org.testng.annotations.Test;

import io.restassured.response.Response;

//as the 4 tests are linked via an id a testng xml file is needed to run these tests

public class deleteuser {
	@Test
	void test_deleteuser(ITestContext context)
	{
		String bearerToken="fom postman";
		//int id=(Integer)context.getAttribute("user_id");
		int id=(Integer)context.getSuite().getAttribute("user_id");//to run the tests indivisually
		
		given()
		.headers("Authorizations","Bearer "+bearerToken);
		.pathparam("id", id)
	
		.when()
			.delete("URL");
		
		.then()
			.statusCode(204);
			.log().all();
	}
}
