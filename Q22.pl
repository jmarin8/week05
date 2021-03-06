#!/usr/bin/perl
use warnings;
use strict;
use Storable qw(retrieve);

my $ret_dna = retrieve('dna');
die "Unable to retrieve from dna!\n" unless defined $ret_dna;
my @arr = @{$ret_dna};
foreach my $i(0 .. 9){
	my $seq = $arr[$i];
	BASE: foreach my $base ( qw/ A C G T / ) {
      if ( $seq =~ /$base{4}/ ) {
        print "4$base run found in $seq\n";
        last BASE;
      }
    }
}
