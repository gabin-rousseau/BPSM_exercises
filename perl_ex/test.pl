#!/usr/bin/perl

#trial perl code applying regex to an array and a file's contente

#safety net parameters
use strict;
use warnings;

#define array of strings with tab separation
print "Reading array...\n";
my @lines = ("Tuesday: Eggs	Friday: Bacon", "Tuesday: Apples	Sunday: Oranges");

#Loop through array elements and print current element if pattern matched
foreach (@lines) {
	if (/A[^bio]ples\tSunday/) {
		print "$_\n";
	} 
};

print "Now reading file...\n";

#open file links. The input is read, a output is created, and so is a log
open(my $in,  "<",  "days_fruits.txt")  or die "Can't open input.txt: $!";
open(my $out, ">",  "tuesday.txt") or die "Can't open output.txt: $!";
open(my $log, ">>", "my.log")     or die "Can't open my.log: $!";

#loop through lines of the input file, print line to output if pattern matched, print the second captured field as well
while (<$in>) {
	if (/(Tuesday)\t(.+)/){
		print $out "$_\n";
		print "$2\n";
	} 

};

#don't forget to close the file links!
close $in or die "$in: $!";
close $out or die "$out: $!";
close $log or die "$log: $!";
