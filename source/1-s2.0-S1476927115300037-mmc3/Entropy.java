//--------------------------------------------------------------------
//NAME: Entropy.java

//DESCRIPTION: Outline Java code used to calculate entropy of rolling windows
//of sequence. Place holders are used to indicate where external
//connections to databases, files and additional code should be 

//DATE: 01/05/2015

//REFERENCE: 
//DNA entropy reveals a significant difference in complexity between
//housekeeping and tissue specific gene promoters
//Thomas et al.,  Computational Biology and Chemistry
//-------------------------------------------------------------------
package bioutils;
import java.util.HashSet;

public class Entropy {
	int[][] seqcnts;
	int[] tots;
	int [] cnts;
	int allseqSize = 15000;
	int noRecs = 12003;
	double[] means;
	HashSet<String> seqs;
	int cnt;
	String allseq, tseq, fName;
	
	public EntropyTP2(){
		//Setup
		seqcnts = new int[noRecs][allseqSize];
		tots = new int[allseqSize];
		means = new double[allseqSize];
		cnts = new int[allseqSize];
		cnt=0;
		//Database Connection, Query and Exception Code goes here
		//
		//Main Loop reads data in 259 byte chunks and populates a hashset with each different value
		try{
			while(rs.next()){
				allseq = rs.getString(1) ;
				seqs = new HashSet<String>();
				for(int i=0;i<(allseqSize - 259);i++){
					tseq = allseq.substring(i, i+259);
					seqs = CalcUnique(tseq);
					cnts[i]++;
					seqcnts[cnt][i] = seqs.size();
					seqs = null;
				}	
				cnt++;
				if(cnt % 100 == 0) System.out.println(cnt + " Records");
			}
		}
		catch(Exception e){
			e.printStackTrace();
			System.exit(1);
		}
		//calculate totals
		for(int j=0;j<noRecs;j++){
			for(int k=0;k<allseqSize;k++){
				tots[k] = tots[k] + seqcnts[j][k];
			}
		}
		//Create Output File
		//
		//
		//
		//

		
		//calculate means
		for(int i=0;i<allseqSize;i++){
			//means[i] = (double) tots[i] / 1000;
			means[i] = (double) tots[i] / cnts[i];
			out.println(i + "," + means[i]);
		}		
		out.close();
	}
	
	private HashSet<String> CalcUnique(String inseq){
		String partseq;
		HashSet<String> s = new HashSet<String>();
		int limit = 256;
		for(int j=0;j<limit;j++){
			partseq = inseq.substring(j, j+subSeqSize);
			s.add(partseq);
		}
		return(s);
	}

}
