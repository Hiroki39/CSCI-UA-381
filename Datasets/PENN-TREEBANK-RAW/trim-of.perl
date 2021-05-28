#!/usr/bin/perl
while (<>) {
    s/.*( [a-zA-Z][a-zA-Z]* of ).*/$1/;
    s/.*:([A-Z][a-z]* of ).*/$1/;
    s/^ //;
    s/ of //;
    tr/[A-Z]/[a-z]/;
    print unless(/wsj\_/);
}
