#!/usr/bin/perl
use warnings;
use strict;
use Storable qw(store);

my @bases = qw/ A C G T /;
my @dna_s;
foreach my $i ( 0 .. 9 ) {
	foreach my $j ( 0 .. 49 ) {
		if($j == 0){
			$dna_s[$i]=$bases[ int( rand(4) ) ];
		}else{
			$dna_s[$i] = "$dna_s[$i]$bases[ int( rand(4) ) ]"
		}
	}
}

store(\@dna_s, 'dna') or die "Can't store %a in /tmp/colors!\n";
print "Saved in file dna";
