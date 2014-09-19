#!/usr/bin/perl -w

# ex:ts=8 sw=4:

use strict;
use CGI qw(:standard);
use Net::Whois::Raw;

my $dom;
my $cg = new CGI;

# Print correct headers
print $cg->header("text/html");
print $cg->start_html("Who is ?");
print $cg->start_form(-method=>"POST",
			-action=>"whois.cgi");
print $cg->textfield(-name=>"dom");
print $cg->submit(-name=>"whois",
		    -value=>"Who is ?");
print $cg->end_form;

# Read POST parameters
$dom = $cg->param('dom');

$Net::Whois::Raw::OMIT_MSG = 1;
if ( defined $dom ) {
	print "<PRE>";
	print whois($dom) . "<BR>\n";
	print "</PRE>";
} else {
	print "Please specify a domain name\n";
}

print $cg->end_html;
