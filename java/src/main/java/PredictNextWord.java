import opennlp.tools.cmdline.PerformanceMonitor;
import opennlp.tools.cmdline.postag.POSModelLoader;
import opennlp.tools.dictionary.Dictionary;
import opennlp.tools.ngram.NGramModel;
import opennlp.tools.postag.POSModel;
import opennlp.tools.postag.POSSample;
import opennlp.tools.postag.POSTaggerME;
import opennlp.tools.sentdetect.SentenceDetectorME;
import opennlp.tools.sentdetect.SentenceModel;
import opennlp.tools.tokenize.Tokenizer;
import opennlp.tools.tokenize.TokenizerME;
import opennlp.tools.tokenize.TokenizerModel;
import opennlp.tools.tokenize.WhitespaceTokenizer;
import opennlp.tools.util.InvalidFormatException;
import opennlp.tools.util.ObjectStream;
import opennlp.tools.util.PlainTextByLineStream;
import opennlp.tools.util.StringList;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.StringReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;

public class PredictNextWord {
    public static void main(String[] args) throws IOException {
        // runTokenize();
        String text = "Detaljhandelsföretag sjönk på Hongkongbörsen. Protesterna väntas slå mot detaljhandeln bland annat genom att turister från fastlands-Kina håller sig borta från Hong Kong under firandet av Kinas nationaldag och de omgivande helgdagarna, då protesterna väntas kulminera.";
        String[] sentences = getSentences(text);
        ArrayList<String> sentencez = new ArrayList<String>(Arrays.asList(sentences));
        for (String sent : sentencez) {
            System.out.println(sent);
        }
        createNgrams(sentencez, 0);
    }

    public static void runTokenize() throws IOException {
        String stringToTokenize = "Hej! Hur är läget? Jag heter Frej.";
        String[] tokens = Tokenize(stringToTokenize);
        for (String a : tokens) {
            System.out.println(a);
        }
    }

    public static String[] Tokenize(String stringToTokenize) throws IOException {
        InputStream is = PredictNextWord.class.getResourceAsStream("se-token.bin");
        TokenizerModel model = new TokenizerModel(is);
        Tokenizer tokenizer = new TokenizerME(model);
        String[] result =  tokenizer.tokenize(stringToTokenize);
        is.close();
        return result;
    }

    public static String[] getSentences(String text) throws InvalidFormatException,
            IOException {
        InputStream is = PredictNextWord.class.getResourceAsStream("se-sent.bin");
        SentenceModel model = new SentenceModel(is);
        SentenceDetectorME sentenceDetector = new SentenceDetectorME(model);
        String sentences[] = sentenceDetector.sentDetect(text);
        is.close();
        return sentences;
    }

    public static void createNgrams(ArrayList<String> list, int cutoff) {
        try {
            NGramModel ngramModel = new NGramModel();
            POSModel model = new POSModelLoader().load(new File(PredictNextWord.class.getResource("se-pos-maxent.bin").getPath()));
            PerformanceMonitor perfMon = new PerformanceMonitor(System.err, "sent");
            POSTaggerME tagger = new POSTaggerME(model);
            perfMon.start();
            for (int i = 0; i < list.size(); i++) {
                String inputString = list.get(i);
                ObjectStream<String> lineStream = new PlainTextByLineStream(new StringReader(inputString));
                String line;
                while ((line = lineStream.read()) != null) {
                    String whitespaceTokenizerLine[] = WhitespaceTokenizer.INSTANCE.tokenize(line);
                    String[] tags = tagger.tag(whitespaceTokenizerLine);
                    POSSample sample = new POSSample(whitespaceTokenizerLine, tags);
                    perfMon.incrementCounter();
                    String words[] = sample.getSentence();
                    if(words.length > 0) {
                        for(int k = 2; k < 3; k++) {
                            ngramModel.add(new StringList(words), k, k);
                        }
                    }
                }
            }
            ngramModel.cutoff(cutoff, Integer.MAX_VALUE);
            System.out.println("ngram size " + ngramModel.size());
            Iterator<StringList> it = ngramModel.iterator();
            while (it.hasNext()) {
                StringList strList = it.next();
                System.out.println(strList.toString());
            }
            perfMon.stopAndPrintFinalResult();
        }catch(Exception e) {
            System.out.println(e.toString());
        }
    }
}
