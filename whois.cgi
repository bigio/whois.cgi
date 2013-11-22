#!/usr/bin/perl -w

use strict;
use CGI qw(:standard);
use Net::Whois::Raw;

my $query = new CGI;

# Print correct headers
print "Content-type: text/html\n\n";
print "<HTML><BODY>\n";
print "<FORM ACTION='whois.cgi' METHOD='POST'>\n";
print "<INPUT TYPE='TEXT' NAME='dom'>\n";
print "<INPUT TYPE='SUBMIT' NAME='whois' VALUE='Who is ?'>\n";
print "</FORM>\n";

# Read POST parameters
my $dom = $query->param('dom');

$Net::Whois::Raw::OMIT_MSG = 1;
if ( $dom ne "" ) {
	print "<PRE>";
	print whois($dom) . "<BR>\n";
	print "</PRE>";
} else {
	print "Please specify a domain name\n";
}

print "</BODY></HTML>";
