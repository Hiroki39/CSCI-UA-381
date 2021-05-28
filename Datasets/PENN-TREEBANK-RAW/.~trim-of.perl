#!/usr/bin/perl
while (<>) {
    s/.*([a-z]* of )/$1/;
    print;
}
