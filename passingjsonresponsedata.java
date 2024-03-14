package day4;

import static io.restassured.RestAssured.*;
import static io.restassured.matcher.RestAssuredMatchers.*;
import static org.hamcrest.Matchers.*;

import java.util.Map;

import org.json.JSONObject;
import org.testng.Assert;
import org.testng.annotations.Test;

import io.restassured.response.Response;

public class passingjsonresponsedata 
{
	@Test
	void testjsonresponse() 
	{
		//Approach1
		/*given()
			.contentType("contentType.JSON")
		
		.when()
			.get("http://localhosr:3000/store")
		
		.then()
			.statusCode(200)
			.header("Content-Type", "application/json; charset=utf-8")
			.body("book[3].title, equalTo("The Lord of the Rings"));*/
		
		//Approach2
		Response res=given()
		.contentType("contentType.JSON")
		
		.when()
		.get("http://localhosr:3000/store");
		
		Assert.assertEquals(res.getStatusCode(),200);
		Assert.assertEquals(res.header("Content-Type","application/json; Charset=utf-8");
		bookname= res.jsonPath().get("book[3].title").toString();
		Assert.assertEquals)bookname,"The Lord of the rings");
		
		//Approach3
		Response res=given()
		.contentType("contentType.JSON")
				
		.when()
		.get("http://localhosr:3000/store");
		
		JSONObject jo = new JSONobject(res.toString()); // converting response to json object type
		//search for title of the book 
		boolean ststus= false:
		for(int i=0;i<jo.getJSONArray("book).length;i++)
		{
			String booktitle = jo.getJSONArray("book").getJSONObject(i).get("title").toString();
			System.out.println(booktitle);
			if (booktitle.equals("The Lord of the rings"));
			{
				status = true;
				break;
			}
			Assert.assertEquals(status,true);
			//validate total price of books
			double totalprice = 0;
			for(int i=0;i<jo.getJSONArray("book").length;i++)
					{
						String price = jo.getJSONArray("books").getJSONObject(i).get("price").toString();
						totalprice= totalprice + Double.parseDouble(price);
						Assert.assertEquals(totalprice,53.92);
					}
			
		}
		
		
		
		
			
	}
	
	
}
