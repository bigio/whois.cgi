#!/usr/bin/perl

use strict;
use warnings;

use Mojolicious::Lite;
use Net::Whois::Raw;

get '/' => sub {
  my $c = shift;
  my $whois_res;
  my $dom = $c->param('dom');
  $Net::Whois::Raw::OMIT_MSG = 1;
  if (defined $dom) {
    eval {
      $whois_res = whois($dom);
    };
    if ( not defined $whois_res ) {
      $whois_res = "Domain $dom not supported";
    }
  }
  $c->stash(dom => $dom, whois_res => $whois_res);
  $c->render(template => 'whois');
};
app->secrets(['whois.cgi']);
app->start;
