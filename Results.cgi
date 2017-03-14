#!C:/Perl64/bin/perl.exe

#    	  	 
#	Name: Michael Shohdy 
#	Course: 443
#  	Assignment: #3
#

###################
#print table

print "Content-type: text/html\n\n";-

	print "<html><head><title>Survey Log</title><head>";
	print "<body><table border=3 bordercolor='blue'>";
	print "<tr bgcolor='#CDCDFF'><td>#</td><td>Q1</td><td>Q2</td><td>Q3</td>";
	print "<td>Q4</td><td>Q5</td><td>Q6</td></tr><tr>";
	
	open(FILE,"survey_data.txt") or &dienice("Cant open");
	@lines = <FILE>;
	close(FILE);
	
	foreach (@lines)
	{
		#chomp;
		($Q1,$Q2,$Q3,$Q4,$Q5,$Q6) = (split(/\|/));
		$i++; #counter
		
		print ("<tr bordercolor='purple'><td>$i</td><td>$Q1</td><td>$Q2</td><td>$Q3</td><td>$Q4</td><td>$Q5</td><td>$Q6</td></tr>");
	}
	print "</table></body></html>";

exit(0);