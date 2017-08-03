import java.io.FileNotFoundException;
import java.io.IOException;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import java.io.PrintWriter;
public class JSoup_Test1 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		PrintWriter myWriter = new PrintWriter("MovieList.txt");
		try {
		Document doc= Jsoup.connect("http://www.imdb.com/list/ls055386972/").userAgent("Chrome/17.0").get();
		Elements temp=doc.select("div.info");
		
		int i=0;
		for(Element movieList:temp)
		{
			i++;
			myWriter.println(i + ""+ movieList.getElementsByTag("a").first().text());
			myWriter.flush();
			myWriter.close();
		}
		
		
		
		}
		
		catch (IOException e) {
			e.printStackTrace();
		}
		
		
	}

}
