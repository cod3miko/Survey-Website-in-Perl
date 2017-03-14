#!C:/Perl64/bin/perl.exe

#    	  	 
#	Name: Michael Shohdy 
#	Course: 443
#  	Assignment: #3
#

###################
#info processing

if ($ENV{'REQUEST_METHOD'} eq "POST") {
    $form_size = $ENV{'CONTENT_LENGTH'};
    read (STDIN, $form_data, $form_size);
  }
  else
     {$form_data = $ENV{'QUERY_STRING'};}

  $form_data =~ s/%([\dA-Fa-f][\dA-Fa-f])/pack ("C", hex ($1))/eg;
  @fields = (split(/&/, $form_data));
  $size = @fields;

  for ($i=0; $i < $size; $i++){
     ($key, $value) = (split (/=/, $fields[$i]));
      $value =~ s/[;<>\(\)\{\}\*\|'`\&\$!#:"\\]/\ /g;
      $value =~ s/[+]/\ /g;
      $my_hash{$key}=$value;
   }

###################
#CGI.pm

use CGI;
$mycgi= CGI::new();

$Q1 = $mycgi->param('Q1');
$Q2 = $mycgi->param('Q2');
$Q3 = $mycgi->param('Q3');
$Q4 = $mycgi->param('Q4');
$Q5 = $mycgi->param('Q5');
$Q6 = $mycgi->param('Q6');

$p = $mycgi->param('Prev');
$n = $mycgi->param('Next');

###################
#radio buttons

#radio for question 2 radio_groupQ2
@values = ("1","2","3","4","5");
@labels = ("Not at all","","Somewhat","","Extremely");
$radnum = @values;
foreach $el(@values){ $aux{$el} = ""; }
@radios =  $mycgi->radio_group(-name=>'Q2',-values=>\@values,-labels=>\%aux,-default=>"3" );
$row1 = ""; $row2=""; $row3="";
$tds="text-align:center;width:80px";
for($i=0;$i<$radnum;$i++){
    $row1 .= $mycgi->td({-style=>$tds},$radios[$i]);
    $row2 .= $mycgi->td({-style=>$tds},$values[$i]);
    $row3 .= $mycgi->td({-style=>$tds},$labels[$i]);
}
#radio2 for question 3 radio_groupQ3
@values2 = ("1","2","3","4","5");
@labels2 = ("Not at all","","Somewhat","","Extremely");
$radnum2 = @values2;
foreach $el2(@values2){ $aux2{$el2} = ""; }
@radios2 =  $mycgi->radio_group(-name=>'Q3',-values=>\@values2,-labels=>\%aux2,-default=>"3" );
$r2row1 = ""; $r2row2=""; $r2row3="";
$tds="text-align:center;width:80px";
for($i=0;$i<$radnum2;$i++){
    $r2row1 .= $mycgi->td({-style=>$tds},$radios2[$i]);
    $r2row2 .= $mycgi->td({-style=>$tds},$values2[$i]);
    $r2row3 .= $mycgi->td({-style=>$tds},$labels2[$i]);
}
#radio3 for question 4 radio_groupQ4
@values3 = ("1","2","0");
@labels3 = ("No","Yes","N/A");
$radnum3 = @values3;
foreach $el3(@values3){ $aux3{$el3} = ""; }
@radios3 =  $mycgi->radio_group(-name=>'Q4',-values=>\@values3,-labels=>\%aux3,-default=>"0" );
$r3row1 = ""; $r3row2=""; $r3row3="";
$tds="text-align:center;width:80px";
for($i=0;$i<$radnum3;$i++){
    $r3row1 .= $mycgi->td({-style=>$tds},$radios3[$i]);
    $r3row2 .= $mycgi->td({-style=>$tds},$values3[$i]);
    $r3row3 .= $mycgi->td({-style=>$tds},$labels3[$i]);
}

###################
#"if prev is set" decrease size by 2 fields 
#special case added for field of 3

if($p eq "Prev")
	{if($size == 3){$size = 0;}
	else 
	{$size = $size-2;}}
	
#to preserve state
if ($n eq "Next")
	{$size = $size;}
	
###################
#print html pgs
#print "Content-type: text/html\n\n";

if($size == 0)
{
	#produce Q1
	print 
		$mycgi->header,
		$mycgi->start_html(
			-title=> 'Question 1', 
			-style=>{-code=>'body{text-align:center; overflow-y:scroll; scrollbar-track-color:#ABACFF; scrollbar-face-color:#AAAAAA;}'}, #permanent scrollbar w css (only works in IE)
			-bgcolor=>'#ABACEF'),
		$mycgi->start_form( 
			-method=>'get', 
			-action=>'http://localhost/cgi-bin/Survey.cgi'),
		#Progress bar
		$mycgi->div({-style=>'float:right'},
			$mycgi->div({-style=>'position:relative; background-color:#ABACEF; width:100px; height:12px; border:1px solid black;font-family:arial; font-size:7pt; font-weight:bold; white-space:pre'},'17%             ',
				$mycgi->div({-style=>'position:absolute; top:0; left:0; width:15%; height:12px; background:linear-gradient(to right,#ABACFF,#8A89E6)'},))),
		#page buttons
		$mycgi->div({-style=>'float:right'}, 
			$mycgi->submit(
				-style=>'background-color:#ABACEF; border:0; cursor:pointer; font-family:arial; margin:-5px',
				-name=> 'next', -value=> 'Next'), $mycgi->span('&rtrif;')),
		$mycgi->end_div,
		#Question 1
		$mycgi->p({-style=>'min-height:5em'}), #to place the question further down
		$mycgi->p({-style=>'font-family:arial; font-size:14pt'},
			'1. Please enter your name:'),
		$mycgi->hr,
			$mycgi->textfield(
			-style=>'background-color:#ABACEF',
			-name=>'Q1', -size=>'20'),
		$mycgi->end_form,
		$mycgi->end_html;
}

elsif($size == 2)
{
	#produce Q2
	print 
		$mycgi->header,
		$mycgi->start_html(
			-title=> 'Question 2', 
			-style=>{-code=>'body{text-align:center; overflow-y:scroll; scrollbar-track-color:#ABACFF; scrollbar-face-color:#AAAAAA;}'}, #permanent scrollbar w css (only works in IE)
			-bgcolor=>'#ABACEF'),
		$mycgi->start_form(
			-method=>'get', 
			-action=>'http://localhost/cgi-bin/Survey.cgi'),
		#Progress bar
		$mycgi->div({-style=>'float:right'},
			$mycgi->div({-style=>'position:relative; width:100px; height:12px; border:1px solid black;font-family:arial; font-size:7pt; font-weight:bold'},
				$mycgi->div({-style=>'position:absolute; top:0; left:0; width:25%; height:12px; background:linear-gradient(to right,#ABACFF,#7571D0); white-space:pre'},'       33%',)),
		#page buttons
		$mycgi->div({-style=>'float:right'}, 
			$mycgi->span('&ltrif;'),
			$mycgi->submit(
				-style=>'background-color:#ABACEF; border:0; cursor:pointer; font-family:arial; margin:-5px',
				-name=> 'Prev', -value=> 'Prev'),
			$mycgi->submit(
				-style=>'background-color:#ABACEF; border:0; cursor:pointer; font-family:arial; margin:-5px',
				-name=> 'Next', -value=> 'Next'), $mycgi->span('&rtrif;'))),
		$mycgi->end_div,
		#question 2
		$mycgi->p({-style=>'min-height:5em'}), #to place the question further down
		$mycgi->p({-style=>'font-family:arial; font-size:14pt'},
			'2. Do you find the information included within this web site useful?'),
		$mycgi->hr,
		$mycgi->start_table(
			{-style=>'margin:0px auto; font-family:arial; font-size:10pt; border:2px solid; background:#8482FD;'}),
			$mycgi->Tr( $row1 ), $mycgi->Tr( $row2 ), $mycgi->Tr( $row3 ),
		$mycgi->end_table,
		#pass hidden vals
		$mycgi->hidden(-name=> 'Q1', -default=>$my_hash{Q1}),		
		$mycgi->end_form;
		$mycgi->end_html;
}

elsif($size == 3)
{
	#produce Q3
	print 
		$mycgi->header,
		$mycgi->start_html(
			-title=> 'Question 3', 
			-style=>{-code=>'body{text-align:center; overflow-y:scroll; scrollbar-track-color:#ABACFF; scrollbar-face-color:#AAAAAA;}'}, #permanent scrollbar w css (only works in IE)
			-bgcolor=>'#ABACEF'),
		$mycgi->start_form( 
			-method=>'get', 
			-action=>'http://localhost/cgi-bin/Survey.cgi'),
		#Progress bar
		$mycgi->div({-style=>'float:right'},
			$mycgi->div({-style=>'position:relative; width:100px; height:12px; border:1px solid black;font-family:arial; font-size:7pt; font-weight:bold'},
				$mycgi->div({-style=>'position:absolute; top:0; left:0; width:50%; height:12px; background:linear-gradient(to right,#ABACFF,#5958C0); white-space:pre'},'       50%',)),
		#page buttons
		$mycgi->div({-style=>'float:right'},
			$mycgi->span('&ltrif;'),
			$mycgi->submit(
				-style=>'background-color:#ABACEF; border:0; cursor:pointer; font-family:arial; margin:-5px',
				-name=> 'Prev', -value=> 'Prev'),
			$mycgi->submit(
				-style=>'background-color:#ABACEF; border:0; cursor:pointer; font-family:arial; margin:-5px',
				-name=> 'Next', -value=> 'Next'), $mycgi->span('&rtrif;'))),
		$mycgi->end_div,
		#Question 3
		$mycgi->p({-style=>'min-height:5em'}), #to place the question further down
		$mycgi->p({-style=>'font-family:arial; font-size:14pt'},
			'3. Is the web site easy to navigate?'),
		$mycgi->hr,
		$mycgi->start_table(
			{-style=>'margin:0px auto; font-family:arial; font-size:10pt; border:2px solid; background:#8482FD;'}),
		$mycgi->Tr( $r2row1 ), $mycgi->Tr( $r2row2 ), $mycgi->Tr( $r2row3 ),
		$mycgi->end_table,
		#pass hidden vals
		$mycgi->hidden(-name=> 'Q2', -default=>$my_hash{Q2}),
		$mycgi->hidden(-name=> 'Q1', -default=>$my_hash{Q1}),		
		$mycgi->end_form;
		$mycgi->end_html;
}

elsif($size == 4)
{
	#produce Q4
	print 
		$mycgi->header,
		$mycgi->start_html(
			-title=> 'Question 4', 
			-style=>{-code=>'body{text-align:center; overflow-y:scroll; scrollbar-track-color:#ABACFF; scrollbar-face-color:#AAAAAA;}'}, #permanent scrollbar w css (only works in IE)
			-bgcolor=>'#ABACEF'),
		$mycgi->start_form( 
			-method=>'get', 
			-action=>'http://localhost/cgi-bin/Survey.cgi'),
		#Progress bar
		$mycgi->div({-style=>'float:right'},
			$mycgi->div({-style=>'position:relative; width:100px; height:12px; border:1px solid black;font-family:arial; font-size:7pt; font-weight:bold'},
				$mycgi->div({-style=>'position:absolute; top:0; left:0; width:70%; height:12px; background:linear-gradient(to right,#ABACFF,#423FA8); white-space:pre'},'       67%',)),
		#page buttons
		$mycgi->div({-style=>'float:right'},
			$mycgi->span('&ltrif;'),
			$mycgi->submit(
				-style=>'background-color:#ABACEF; border:0; cursor:pointer; font-family:arial; margin:-5px',
				-name=> 'Prev', -value=> 'Prev'),
			$mycgi->submit(
				-style=>'background-color:#ABACEF; border:0; cursor:pointer; font-family:arial; margin:-5px',
				-name=> 'Next', -value=> 'Next'), $mycgi->span('&rtrif;'))),
		$mycgi->end_div,		
		#Question 4
		$mycgi->p({-style=>'min-height:5em'}), #to place the question further down
		$mycgi->p({-style=>'font-family:arial; font-size:14pt'},
			'4. Were you able to find the information you were looking for?'),
		$mycgi->hr,
		$mycgi->start_table(
			{-style=>'margin:0px auto; font-family:arial; font-size:10pt; border:2px solid; background:#8482FD;'}),
		$mycgi->Tr( $r3row1 ), $mycgi->Tr( $r3row2 ), $mycgi->Tr( $r3row3 ),
		$mycgi->end_table,
		#pass hidden vals
		$mycgi->hidden(-name=> 'Q3', -default=>$my_hash{Q3}),
		$mycgi->hidden(-name=> 'Q2', -default=>$my_hash{Q2}),
		$mycgi->hidden(-name=> 'Q1', -default=>$my_hash{Q1}),
		$mycgi->end_form;
		$mycgi->end_html;
}

elsif($size == 5)
{
	#produce Q5
	print
		$mycgi->header,
		$mycgi->start_html(
			-title=> 'Question 5',
			-style=>{-code=>'body,textarea{text-align:center; overflow-y:scroll; scrollbar-track-color:#ABACFF; scrollbar-face-color:#AAAAAA;}'}, #permanent scrollbar w css (only works in IE)
			-bgcolor=>'#ABACEF'),
		$mycgi->start_form(
			-method=>'get',
			-action=>'http://localhost/cgi-bin/Survey.cgi'),
		#Progress bar
		$mycgi->div({-style=>'float:right'},
			$mycgi->div({-style=>'position:relative; width:100px; height:12px; border:1px solid black;font-family:arial; font-size:7pt; font-weight:bold'},
				$mycgi->div({-style=>'position:absolute; top:0; left:0; width:85%; height:12px; background:linear-gradient(to right,#ABACFF,#282995); white-space:pre'},'83%',)),
		#page buttons
		$mycgi->div({-style=>'float:right'},
			$mycgi->span('&ltrif;'),
			$mycgi->submit(
				-style=>'background-color:#ABACEF; border:0; cursor:pointer; font-family:arial; margin:-5px',
				-name=> 'Prev', -value=> 'Prev'),
			$mycgi->submit(
				-style=>'background-color:#ABACEF; border:0; cursor:pointer; font-family:arial; margin:-5px',
				-name=> 'Next', -value=> 'Next'), $mycgi->span('&rtrif;'))),
		$mycgi->end_div,
		#Question 5	
		$mycgi->p({-style=>'min-height:5em'}), #to place the question further down
		$mycgi->p({-style=>'font-family:arial; font-size:14pt'},
			'5. What other information would you like to include in this website?'),
		$mycgi->hr,
		$mycgi->textarea(
			-style=>'background-color:#ABACEF',
			-name=>'Q5', 
			-rows=>'5',
			-columns=>'50'),
		#pass hidden vals
		$mycgi->hidden(-name=> 'Q4', -default=>$my_hash{Q4}),
		$mycgi->hidden(-name=> 'Q3', -default=>$my_hash{Q3}),
		$mycgi->hidden(-name=> 'Q2', -default=>$my_hash{Q2}),
		$mycgi->hidden(-name=> 'Q1', -default=>$my_hash{Q1}),
		$mycgi->end_form,
		$mycgi->end_html;
}

elsif($size == 6)
{
	#produce Q6
	print 
		$mycgi->header,
		$mycgi->start_html(
			-title=> 'Question 6', 
			-style=>{-code=>'body,textarea{text-align:center; overflow-y:scroll; scrollbar-track-color:#ABACFF; scrollbar-face-color:#AAAAAA;}'}, #permanent scrollbar w css (only works in IE)
			-bgcolor=>'#ABACEF'),
		$mycgi->start_form(
			-method=>'get', 
			-action=>'http://localhost/cgi-bin/Survey.cgi'),
		#Progress bar
		$mycgi->div({-style=>'float:right'},
			$mycgi->div({-style=>'position:relative; width:100px; height:12px; border:1px solid black;font-family:arial; font-size:7pt; font-weight:bold'},
				$mycgi->div({-style=>'position:absolute; top:0; left:0; width:100%; height:12px; background:linear-gradient(to right,#ABACFF,#282995); white-space:pre'},'100%',)),
		#page buttons
		$mycgi->div({-style=>'float:right'},
			$mycgi->span('&ltrif;'),
			$mycgi->submit(
				-style=>'background-color:#ABACEF; border:0; cursor:pointer; font-family:arial; margin:-5px',
				-name=> 'Prev', -value=> 'Prev'),
			$mycgi->submit(
				-style=>'background-color:#ABACEF; border:0; cursor:pointer; font-family:arial; margin:-5px',
				-name=> 'Next', -value=> 'Next'), $mycgi->span('&rtrif;'))),
		$mycgi->end_div,
		#question 6
		$mycgi->p({-style=>'min-height:5em'}), #to place the question further down
		$mycgi->p({-style=>'font-family:arial; font-size:14pt'},
			'6. What suggestions might you have for web site improvement?'),
		$mycgi->hr,
		$mycgi->textarea(
			-style=>'background-color:#ABACEF',
			-name=>'Q6', 
			-rows=>'5',
			-columns=>'50'),
		#pass hidden vals
		$mycgi->hidden(-name=> 'Q5', -default=>$my_hash{Q5}),
		$mycgi->hidden(-name=> 'Q4', -default=>$my_hash{Q4}),		
		$mycgi->hidden(-name=> 'Q3', -default=>$my_hash{Q3}),		
		$mycgi->hidden(-name=> 'Q2', -default=>$my_hash{Q2}),		
		$mycgi->hidden(-name=> 'Q1', -default=>$my_hash{Q1}),
		$mycgi->end_form,
		$mycgi->end_html;
}

else
{
	#produce thank you page
	print 
		$mycgi->header,
		$mycgi->start_html(
			-title=> 'Thank you', 
			-bgcolor=>'#ABACEF'),
		$mycgi->p({-style=>'min-height:5em'}), #to place the question further down
		$mycgi->p({-style=>'font-family:arial; font-size:14pt; font-weight:bold; white-space:pre'},
			'        Thank you for your input.'),
		$mycgi->hr,
		$mycgi->end_html;
}

###################
#print data to file aka "flat file database"

if($Q6)
{
	#for questions 5 and 6 special case:new line characters
	$my_hash{Q6} =~ s/\n/<br>/g;
	$my_hash{Q5} =~ s/\n/<br>/g;

	open(OUT, ">>survey_data.txt") or &dienice("Cant output file");
	print OUT $my_hash{Q1}, "|";
	print OUT $my_hash{Q2}, "|";
	print OUT $my_hash{Q3}, "|";
	print OUT $my_hash{Q4}, "|";
	print OUT $my_hash{Q5}, "|";
	print OUT $my_hash{Q6};
	print OUT "\n";
	close(OUT);
}
###################
#exit system
exit(0);
