package day8;

import static io.restassured.RestAssured.*;
import static io.restassured.matcher.RestAssuredMatchers.*;
import static org.hamcrest.Matchers.*;

import org.json.JSONObject;
import org.testng.ITestContext;
import org.testng.annotations.Test;

import io.restassured.response.Response;
//as the 4 tests are linked via an id a testng xml file is needed to run these tests

public class edituser {
	@Test
	void test_updateuser(ITestContext context)
	{
		Faker faker = new Faker();
		JSONObject data = new JSONobject();
		
		data.put("name",fake.name().fullname());
		data.put("gender", "Female"); //can add more
		data.put("email".faker.internet().emailaddress());
		data.put("status", "active");
		
		String bearerToken=" add token from postman";
		//int id=(Integer)context.getAttribute("user_id");
		int id=(Integer)context.getSuite().getAttribute("user_id");//to run the tests indivisually
		
		Response id= given()
			.headers("Authorizations","Bearer "+bearerToken)
			.contentType("application/json")
			.pathParam("id",id);
			.body(data.toString())
			
		.when()
			.put("URL/{id}");
			.jsonPath().getint("id");
		
		.then()
			.statusCode(200);
			.log().all();
	)

}
