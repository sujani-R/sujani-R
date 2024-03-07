package day3;

import static io.restassured.RestAssured.*;
import static io.restassured.matcher.RestAssuredMatchers.*;
import static org.hamcrest.Matchers.*;

import java.util.Map;

import org.testng.annotations.Test;

import io.restassured.http.Header;
import io.restassured.http.Headers;
import io.restassured.response.Response;

public class logdemo 
{
	@Test
	void testlogs()
	{
		given()
		.when()
			.get("https://reqres.in/")
		.then()
			.log().body(); //prints only body from response
			//.log().all();
			//.log().cookies()//prints cookies from response
			//.log().headers();
		
	}
	

}
