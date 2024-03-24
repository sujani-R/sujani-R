package day8;

import static io.restassured.RestAssured.*;
import static io.restassured.matcher.RestAssuredMatchers.*;
import static org.hamcrest.Matchers.*;

import org.json.JSONObject;
import org.testng.ITestContext;
import org.testng.annotations.Test;

import io.restassured.response.Response;
//as the 4 tests are linked via an id a testng xml file is needed to run these tests
@Test
public class createuser {

	void test_createuser(ITestContext context)
	{
		Faker faker = new Faker();
		JSONObject data = new JSONobject();
		
		data.put("name",fake.name().fullname());
		data.put("gender", "male"); //can add more
		data.put("email".faker.internet().emailaddress());
		data.put("status", "inactive");
		
		String bearerToken=" add token from postman";
		
		Response id= given()
			.headers("Authorizations","Bearer "+bearerToken)
			.contentType("application/json")
			.body(data.toString())
			
		.when()
			.post("URL");
			.jsonPath().getint("id");
			
		System.out.println(id);
		//context.setAttribute("user_id",  id);
		context.getSuite().setAttribute("user_id",  id); //to run the tests indivisually
	)
	}
}
