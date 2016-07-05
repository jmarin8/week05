#! /opt/perl/bin/perl
use warnings;
use strict;

use CGI (':standard');

my $title = 'Generate random sequence';
print header, start_html($title), h1($title);

# handle processing of form if this is a submission
if ( param('submit') ) {
	my $sequence = param('sequence');

	print p("Selected sequence is $sequence.");

	my (@amino_acids) = qw/A C D E F G H I K L M N P Q R S T V W Y/;
	my @nucleotide = qw/ A C G T /;
	my $i;
	if ( $sequence eq 'Amino acid protein sequence' ) {
		foreach my $j ( 0 .. 49 ) {
			if ( $j == 0 ) {
				$i = $amino_acids[ int( rand(20) ) ];
			}
			else {
				$i = "$i$amino_acids[ int( rand(20) ) ]";
			}
		}
	}
	else {
		foreach my $j ( 0 .. 49 ) {
			if ( $j == 0 ) {
				$i = $nucleotide[ int( rand(4) ) ];
			}
			else {
				$i = "$i$nucleotide[ int( rand(4) ) ]";
			}
		}
	}
	print $i;

	print hr();
}

# and then print out the base form regardless of whether this is the
# first time or the tenth
my $url = url();
print start_form( -method => 'GET', action => $url ),
  p(
	"Select Sequence "
	  . radio_group(
		-name   => 'sequence',
		-values => [ 'Nucleotide DNA sequence ', 'Amino acid protein sequence' ]
	  )
  ),
  p( submit( -name => 'submit', value => 'Submit' ) ),
  end_form(),
  end_html();
