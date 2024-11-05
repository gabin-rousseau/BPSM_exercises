#!/usr/bin/perl

use strict;
use warnings;

print "Reading array...\n";
my @lines = ("Tuesday: Eggs	Friday: Bacon", "Tuesday: Apples	Sunday: Oranges");

foreach (@lines) {
	if (/A[^bio]ples\tSunday/) {
		print "$_\n";
	} 
};

print "Now reading file...\n";

open(my $in,  "<",  "days_fruits.txt")  or die "Can't open input.txt: $!";
open(my $out, ">",  "tuesday.txt") or die "Can't open output.txt: $!";
open(my $log, ">>", "my.log")     or die "Can't open my.log: $!";

while (<$in>) {
	if (/(Tuesday)\t(.+)/){
		print $out "$_\n";
		print "$2\n";
	} 

};

close $in or die "$in: $!";
close $out or die "$out: $!";
close $log or die "$log: $!";
