package day2;

/*static packages*/
import static io.restassured.RestAssured.*;
import static io.restassured.matcher.RestAssuredMatchers.*;
import static org.hamcrest.Matchers.*;
import java.util.HashMap;


public class postrequestbody 
{/* using hashmap*/
	//@Test
	void testhashmap()
	{
		HashMap data= new HashMap();
		data.put("name","scott");
		data.put("location","France");
		data.put("phone", "123456");
		
		String courseArr[]= {"C","C++"};
		data.put("courses", courseArr)
		
		given()
			.contentType("application/json")
			.body(data)
			
		.when()
			.post("https://localhost:3000/students")
		.then()
			.ststusCode(201)
			.body("name", equalTo("scott"))
			.header("Content-Type","application/json; charset=utf-8")
			.log().all();
	}
	
	@Test
	void testdelete()
	{
		given()
		.when()
			.delete("https://localhost:3000/students/4")
		.then()
			.statusCode(200);
		
	}
	//post using org.json library, need to add org.json dependency in pom.xml
		//@Test
		void testjsonlibrary()
		{
			JSONObject data = new JSONObject();
			
			data.put("name","scott");
			data.put("location","France");
			data.put("phone", "123456");
			
			String courseArr[]= {"C","C++"};
			data.put("courses", courseArr)
			
			
			
			given()
				.contentType("application/json")
				.body(data.toString())
				
			.when()
				.post("https://localhost:3000/students")
			.then()
				.ststusCode(201)
				.body("name", equalTo("scott"))
				.header("Content-Type","application/json; charset=utf-8")
				.log().all();
		}
		//using POJO class(plain old java object)
		//@Test
				void testPOJOclass()
				{
					POJO_postrequest data = new POJO_postrequest();
					data.setName("scott");
					data.setLocation("france");
					String coursesArr[]=("C","C**")
					data.setCourses(coursesArray);
					
					given()
						.contentType("application/json")
						.body(data)
						
					.when()
						.post("https://localhost:3000/students")
					.then()
						.ststusCode(201)
						.body("name", equalTo("scott"))
						.header("Content-Type","application/json; charset=utf-8")
						.log().all();
				}
		//using external json file
		//@Test
		void testExternaljsonfile()
		{
			File f= new File{".\\body.json");//loc of json file
			FileReader FR = new FileReader(f);
			JSONTokener jt = new JSONTokener(fr);
			JSONobject data = new JSONObject(jt);
			
			
			given()
			.contentType("application/json")
			.body(data.tostring())
			
		.when()
			.post("https://localhost:3000/students")
		.then()
			.ststusCode(201)
			.body("name", equalTo("scott"))
			.header("Content-Type","application/json; charset=utf-8")
			.log().all();
		}
						{
			
			
			
			
}


