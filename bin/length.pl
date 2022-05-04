#!/use/bin/perl			#perl解析器


$inputFile = $ARGV[0];       #输入文件:fasta
$outputDir = $ARGV[1];       #输出目录


if (@ARGV<2) {
	print "inputfile and outputdir are required!\n";
	exit 1;
}

open(DATA,"$inputFile") or die("Could not open file!!!");
#获取fasta文件名
@input = split(/\//,$inputFile); @fastaname = split(/\./,$input[-1]);
#生成输出文件名
$outputFile = join ("/", $outputDir, join("_", $fastaname[0], "length.txt"));
open(RESULT,">$outputFile");


my%hash,$read;
foreach $line (<DATA>) {
	chomp($line);
	if($line =~ /^>/){  #判断是序列名称行
		$read = $line;
		$hash{$read} = 0;
	}else{
		$hash{$read} += length($line);
	}
}

my$Total_read = 0,$Total_length = 0;
foreach $k(keys %hash){
	#print "$k\t$hash{$k}\n";
	$Total_length = $Total_length+$hash{$k};
	$Total_read = $Total_read+1;
}

print RESULT "Total_read:\t$Total_read\nTotal_length:\t$Total_length";

close(DATA);close(RESULT);
