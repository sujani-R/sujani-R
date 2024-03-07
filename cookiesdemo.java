package day3;

import static io.restassured.RestAssured.*;
import static io.restassured.matcher.RestAssuredMatchers.*;
import static org.hamcrest.Matchers.*;

import java.util.Map;

import org.testng.annotations.Test;

import io.restassured.response.Response;

public class cookiesdemo {
	
	@Test
	void testCookies()
	{
		given()
		
		
		.when()
			.get("https://www.google.com/")
		
		.then()
		//.cookie("AEC","abcmcnkugdierhwlioerwi3uhrhw")//value specified changes everytime
		.log().all(); //hence execution failes and test passes
		
		
	}
	@Test
	void getCookiesinfo()
	{
		Response res=given()
		
		
		.when()
			.get("https://www.google.com/");
		
		//get single cookie info
		//String cookie_value = res.getCookie("AEC");
		//System.out.println("value of cookie is"+ cookie_value);
		//gte all cookie info
		Map<String,String> Cookies_values= res.getCookies();
		System.out.println(Cookies_values.keySet());
		for(String k:Cookies_values.keySet())
		{
			String cookie_value = res.getCookie(k);
			System.out.println(k+ "   " + cookie_value);
		}
		
		
		
		
		
	}

}
