#!/usr/bin/perl -w

use strict;
use CGI qw(:standard);
use Net::Whois::Raw;

my $query = new CGI;

# Print correct headers
print "Content-type: text/html\n\n";
print "<HTML><BODY>";

# Read POST parameters
my $dom = $query->param('dom');

$Net::Whois::Raw::OMIT_MSG = 1;
print whois($dom) . "<BR>\n";

print "</BODY></HTML>";
