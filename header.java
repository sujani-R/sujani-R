package day3;
import static io.restassured.RestAssured.*;
import static io.restassured.matcher.RestAssuredMatchers.*;
import static org.hamcrest.Matchers.*;

import java.util.Map;

import org.testng.annotations.Test;

import io.restassured.http.Header;
import io.restassured.http.Headers;
import io.restassured.response.Response;

public class header {
	
	//@Test
	void testheader()
	{
		given()
		
		
		.when()
			.get("https://www.google.com/")
		
		.then()
			.header("content type", "text/html; Charset=150*8859-1")
			.header("content encoding", "gzip")
			.header("Server", "gws");
	}
	@Test
	void getheaders()
	{
		Response res= given()
		
		
		.when()
			.get("https://www.google.com/");
		
		//get single header info
		String headervalue= res.getHeader("content-Type");
		System.out.println("value of header value" + headervalue);
		
		//get all headers info
		Headers myheaders = res.getHeaders();
		
		for(Header hd:myheaders )
		{
			System.out.println(hd.getName()+"    "+ hd.getValue());
		}
			
			
	}



}
