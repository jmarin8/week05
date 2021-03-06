#!/usr/bin/perl
use warnings; 
use strict;

my @arr1 = ( 1, 2, 3 );
my @arr2 = ( 4, 5, 6 );

my $result = multiply_array( \@arr1, \@arr2 );
print "@$_\n" for @$result;

sub multiply_array {
	my ( $arr1_ref, $arr2_ref ) = @_;

	
	my @result;
	for(my $i=0; $i<scalar @{$arr1_ref}; $i++){
        for(my $j=0; $j<scalar @{$arr2_ref}; $j++){
            my $res = @{$arr1_ref}[$i] * @{$arr1_ref}[$j];
            $result[$i][$j] = $res;
        }
	}
	return \@result;
}
