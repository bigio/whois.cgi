#!/usr/bin/perl -w

# ex:ts=8 sw=4:

use strict;
use CGI qw(:standard);
use Net::Whois::Raw;

my $dom;
my $query = new CGI;

# Print correct headers
print $query->header("text/html");
print $query->start_html("Who is ?");
print $query->start_form(-method=>"POST",
			-action=>"whois.cgi");
print $query->textfield(-name=>"dom");
print $query->submit(-name=>"whois",
		    -value=>"Who is ?");
print $query->end_form;

# Read POST parameters
$dom = $query->param('dom');

$Net::Whois::Raw::OMIT_MSG = 1;
if ( $dom ne "" ) {
	print "<PRE>";
	print whois($dom) . "<BR>\n";
	print "</PRE>";
} else {
	print "Please specify a domain name\n";
}

print $query->end_html;
