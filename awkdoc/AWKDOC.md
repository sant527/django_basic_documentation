   * [<span>AWK</span>](#awk)
   * [<span>AWK syntax</span>](#awk-syntax)
   * [<span>awk '/pattern1/ || /pattern2/{print}'</span>](#awk-pattern1--pattern2print)
   * [<span>The syntax of awk is:</span>](#the-syntax-of-awk-is)
   * [<span>BEGIN block</span>](#begin-block)
   * [<span>Body Block</span>](#body-block)
   * [<span>END BLOCK</span>](#end-block)
   * [<span>EXAMPLES (BEGIN BLOCK)</span>](#examples-begin-block)
   * [<span>EXAMPLE BODY BLOCK</span>](#example-body-block)
   * [<span>DUMPING VARIABLES</span>](#dumping-variables)
   * [<span>FIELDS</span>](#fields)
      * [<span>Example</span>](#example)
      * [<span>NF</span>](#nf)
      * [<span>$0</span>](#0)
      * [<span>EXAMPLE $1 and $0 and regex</span>](#example-1-and-0-and-regex)
      * [<span>Nonconstant Field Numbers</span>](#nonconstant-field-numbers)
      * [<span>Changing the Contents of a Field</span>](#changing-the-contents-of-a-field)
      * [<span>Example print last but one and last fields</span>](#example-print-last-but-one-and-last-fields)
      * [<span>Example muliple print vs single print</span>](#example-muliple-print-vs-single-print)
   * [<span>HOW TO reconstitute the record</span>](#how-to-reconstitute-the-record)
   * [<span>NR</span>](#nr)
   * [<span>EXAMPLE OFS AND FS SET LATE, Setting of variables</span>](#example-ofs-and-fs-set-late-setting-of-variables)
   * [<span>NR VS FNR</span>](#nr-vs-fnr)
   * [<span>EXAMPLE : Print number and File (NR vs count  )</span>](#example--print-number-and-file-nr-vs-count)
   * [<span>Example: </span><span>find any field beginning from 2  which contains word image</span>](#example-find-any-field-beginning-from-2-which-contains-word-image)
   * [<span>Example field</span>](#example-field)
   * [<span>EXAMPLE OF IF and matching each field with ~:</span>](#example-of-if-and-matching-each-field-with-)
   * [<span>RS</span>](#rs)
   * [<span>$0</span>](#0-1)
   * [<span>IGNORECASE</span>](#ignorecase)
   * [<span>EXAMPLE print</span>](#example-print)
   * [<span>REGEX NOT  MATCHING</span>](#regex-not-matching)
   * [<span>EXAMPLE find if contains words OR and AND</span>](#example-find-if-contains-words-or-and-and)
   * [<span>Simply Arithmetic</span>](#simply-arithmetic)
   * [<span>USE shell variable inside awk</span>](#use-shell-variable-inside-awk)
   * [<span>EXAMPLE using function inside awk</span>](#example-using-function-inside-awk)
   * [<span>EXAMPLE substituting in awk gsub</span>](#example-substituting-in-awk-gsub)
   * [<span>EXAMPLE ADD new line after a line</span>](#example-add-new-line-after-a-line)
   * [<span>passing shell variables</span>](#passing-shell-variables)
   * [<span>EXAMPLE How to adding all the numbers in 4th column and print the total value at the end.</span>](#example-how-to-adding-all-the-numbers-in-4th-column-and-print-the-total-value-at-the-end)
   * [<span>How do I print all lines that have three (3) words only?</span>](#how-do-i-print-all-lines-that-have-three-3-words-only)
   * [<span>EXAMPLE Gsub</span>](#example-gsub)
   * [<span>EXAMPLE Processing the delimited files using awk</span>](#example-processing-the-delimited-files-using-awk)
   * [<span>** EXAMPLE The default syntax to read a text file line-by-line using awk is as follows:</span>](#-example-the-default-syntax-to-read-a-text-file-line-by-line-using-awk-is-as-follows)
   * [<span>** EXAMPLE awk define and print variable</span>](#-example-awk-define-and-print-variable)
   * [<span>**EXAMPLE display line number</span>](#example-display-line-number)
   * [<span>EXAMPLE print required lines</span>](#example-print-required-lines)
   * [<span>Here are some ways to get variables in to awk:</span>](#here-are-some-ways-to-get-variables-in-to-awk)
   * [<span>** spliting into files</span>](#-spliting-into-files)
   * [<span>Conditional awk printing</span>](#conditional-awk-printing)
   * [<span>passing variable: Correct, awk won't recogize variables in / /. You can do:</span>](#passing-variable-correct-awk-wont-recogize-variables-in---you-can-do)
   * [<span>  awk - Match a pattern in a file in Linux:</span>](#-awk---match-a-pattern-in-a-file-in-linux)
   * [<span>To get color output from awk, you can use this approach.</span>](#to-get-color-output-from-awk-you-can-use-this-approach)
   * [<span>AWK colors and ANSI graphics </span>](#awk-colors-and-ansi-graphics-)
   * [<span>EXAMPLE OFS</span>](#example-ofs)
   * [<span>How do we get the entire file content printed in other way?</span>](#how-do-we-get-the-entire-file-content-printed-in-other-way)
   * [<span>How to omit the header record and get only the names printed?</span>](#how-to-omit-the-header-record-and-get-only-the-names-printed)
   * [<span> awk - Match a pattern in a file in Linux</span>](#awk---match-a-pattern-in-a-file-in-linux)
   * [<span>3. awk has the getline command which reads the next line from the file.</span>](#3-awk-has-the-getline-command-which-reads-the-next-line-from-the-file)
   * [<span>o print only the line following the pattern without the line matching the pattern:</span>](#o-print-only-the-line-following-the-pattern-without-the-line-matching-the-pattern)
   * [<span>Print multiple lines are selecting</span>](#print-multiple-lines-are-selecting)
   * [<span>Gsub vs sub</span>](#gsub-vs-sub)
   * [<span>AWK: the substr command to select a substring</span>](#awk-the-substr-command-to-select-a-substring)
   * [<span>Match function</span>](#match-function)
   * [<span>EXAMPLE EXIT AFTER 1st RECORD</span>](#example-exit-after-1st-record)
   * [<span>AWK: Access captured group from line pattern</span>](#awk-access-captured-group-from-line-pattern)
   * [<span>EXAMPLE awk print </span>](#example-awk-print-)
   * [<span>EAMPLE print array of match</span>](#eample-print-array-of-match)
* # AWK

* # AWK syntax

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>awk 'condition{action}' file or<br>awk 'condition{action}condition{action}condition{action}' file<br>where condition can be any of:<br><ol><li>a key word like BEGIN or END</li><li>an arithmetic expression like var &lt; 7 or NF or 1</li><li>a regexp comparison like $0 ~ "foo" or $0 ~ /foo/ or /foo/ or $0 ~ var or match($0,/foo/)</li><li>a string comparison like $0 == "foo" or index($0,"foo")</li><li>nothing at all in which case it's assumed to be true when there's an associated action block.</li></ol>and probably other things I'm forgetting to list.<br><br>Eg:<br><br>$ awk '/Linux/{x=NR+2}(NR&lt;=x){print}' file<br>Linux<br>Solaris<br>Aix<br><br><ol><li>Condition{action} = /Linux/{x=NR+2}</li><li>Condition{action} = (NR&lt;=x){print}</li></ol><br><br>C-like syntax would be:<br><br>NR=0<br>x=0<br>While read (file,line)<br>{<br>  NR++<br> -- First condition --<br>  if (line ~ "Linux") {<br>    -- First action --<br>    x = NR+2<br>  }<br><br> -- Second condition --<br>  if (NR &lt;= x) {<br> -- Second action --<br>    print<br>  }<br>}<br><br><br>Eg:<br><br>$ cat tst.awk<br>{<br>    match($0,/^(\s*(\S)\s*)(.*)/,a)<br>    currHead = a[1]<br>    currChar = a[2]<br>    currTail = a[3]<br>}<br>currChar == "#" { indent = currHead }<br>currChar != "#" { indent = (prevChar == "#" ? currHead : indent) }<br>{ printf "%s%s\n", indent, currTail; prevChar = currChar }<br><br>$ awk -f tst.awk file<br># jkakjshkjh<br>  *   drink  (2 spaces *  2 spaces)(non hash starting)<br>  *   biscuit  (1 space * 2 spaces)(non hash starting)<br>  *   paper       (* 1 space)(non has starting)<br>  *   .. (many more lines) of non hash starting<br>  *   tea   (7 spaces * 3 space)(non has starting)<br># happy<br>* cup       (* 1 space)(non has starting)<br>* bat  (2 spaces *  2 spaces)(non hash starting)<br>* scooter  (1 space * 2 spaces)(non hash starting)<br>* .. (many more lines) of non hash starting<br>* disk   (7 spaces * 3 space)(non has starting)<br><br><br>To help you understand the syntax, if I were writing the above in a C-like language then it'd be:<br><br>while ( read(FILENAME,line) ) {                 # awk does this for you<br>    NR++;                                       # awk does this for you<br>    NF = split(line into $1, $2, $3, ... $NF);  # awk does this for you<br>    match(line,/^(\s*(\S)\s*)(.*)/,a);<br>    currHead = a[1];<br>    currChar = a[2];<br>    currTail = a[3];<br>    if (currChar == "#") { indent = currHead; }<br>    if (currChar != "#") { indent = (prevChar == "#" ? currHead : indent); }<br>    printf "%s%s\n", indent, currTail; prevChar = currChar;<br>}                                               # awk does this for you<br><br><br>and in fact you can duplicate that syntax in awks BEGIN section with:<br><br>BEGIN {<br>    filename = ARGV[1]<br>    ARGV[1] = ""<br>    ARGC--<br>    while ( (getline line &lt; filename) &gt; 0) ) {<br>        nr++<br>        nf = split(line,flds)<br>        match(line,/^(\s*(\S)\s*)(.*)/,a)<br>        currHead = a[1]<br>        currChar = a[2]<br>        currTail = a[3]<br>        if (currChar == "#") { indent = currHead }<br>        if (currChar != "#") { indent = (prevChar == "#" ? currHead : indent) }<br>        printf "%s%s\n", indent, currTail; prevChar = currChar<br>    }<br>}<br>but see http://awk.freeshell.org/AllAboutGetline for why not to do that unless you have a very specific need.<br><br><br><br></td></tr></tbody></table>

* # awk '/pattern1/ || /pattern2/{print}'

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>awk '/pattern1/ || /pattern2/{print}'<br><br>Edit<br><br>To be fair, I like lhf's way better via /pattern1|pattern2/ since it requires less typing for the same outcome. However, I should point out that this template cannot be used for logical AND operations, for that you need to use my template which is /pattern1/ &amp;&amp; /pattern2/<br></td></tr></tbody></table>

* # The syntax of awk is:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>awk 'pattern{action}' file<br><br>   where the pattern indicates the pattern or the condition on which the action is to be executed for every line matching the pattern. In case of a pattern not being present, the action will be executed for every line of the file. In case of the action part not being present, the default action of printing the line will be done. Let us see some examples:<br><br></td></tr></tbody></table>

* # BEGIN block

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>BEGIN {awk-commands}<br><br>The begin block gets executed at program startup and is executes only once. This is good place to initialise variables. BEGIN is the AWK keyword and hence it must be in upper case. Please note that this block is optional.<br></td></tr></tbody></table>

* # Body Block

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>/pattern/ {awk-commands}<br><br>OR<br /><br>Condition_check/regexp{action}<br><br>The body block apply AWK commands on every input line. By default AWK execute commands on every line but we can restrict this by providing pattern. Note that there is no keyword for Body block<br></td></tr></tbody></table>

* # END BLOCK

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>END {awk-commands}<br><br>The end block gets executed at the end of program. END is the AWK keyword and hence it must be in upper case. Please note that this block is also optional.<br>Examples<br></td></tr></tbody></table>

* # EXAMPLES (BEGIN BLOCK)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Let us create a file marks.txt which contains the serial number, name of the student, subject name and number of marks obtained.<br><br>1)    Amit     Physics    80<br>2)    Rahul    Maths      90<br>3)    Shyam    Biology    87<br>4)    Kedar    English    85<br>5)    Hari     History    89<br><br>Now let us display the file contents with header by using AWK script.<br><br>[jerry]$ awk 'BEGIN{printf "Sr No\tName\tSub\tMarks\n"} {print}' marks.txt<br><br>When the above code is executed, it will produce the following result.<br><br>Sr No Name     Sub        Marks<br>1)    Amit     Physics    80<br>2)    Rahul    Maths      90<br>3)    Shyam    Biology    87<br>4)    Kedar    English    85<br>5)    Hari     History    89<br><br>At program startup AWK prints header from BEGIN block. Then in body block, it reads a line from a file and executes AWK's print command which just prints the contents on the standard output stream. This process repeats until file is exhausted.<br></td></tr></tbody></table>

* # EXAMPLE BODY BLOCK

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Example<br><br>Consider we have a text file marks.txt to be processed and it has following content:<br><br>1)    Amit     Physics    80<br>2)    Rahul    Maths      90<br>3)    Shyam    Biology    87<br>4)    Kedar    English    85<br>5)    Hari     History    89<br><br>Let's display complete content of the file using AWK as follows:<br><br>[jerry]$ awk '{print}' marks.txt <br><br>On executing the above code, you get the following result:<br><br>1)    Amit     Physics    80<br>2)    Rahul    Maths      90<br>3)    Shyam    Biology    87<br>4)    Kedar    English    85<br>5)    Hari     History    89<br><br></td></tr></tbody></table>

* # DUMPING VARIABLES

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>The --dump-variables[=file] option<br><br>It prints a sorted list of global variables and their final values to file. The default file is awkvars.out.<br><br>[jerry]$ awk --dump-variables ''<br>[jerry]$ cat awkvars.out <br><br>On executing the above code, you get the following result:<br><br>ARGC: 1<br>ARGIND: 0<br>ARGV: array, 1 elements<br>BINMODE: 0<br>CONVFMT: "%.6g"<br>ERRNO: ""<br>FIELDWIDTHS: ""<br>FILENAME: ""<br>FNR: 0<br>FPAT: "[^[:space:]]+"<br>FS: " "<br>IGNORECASE: 0<br>LINT: 0<br>NF: 0<br>NR: 0<br>OFMT: "%.6g"<br>OFS: " "<br>ORS: "\n"<br>RLENGTH: 0<br>RS: "\n"<br>RSTART: 0<br>RT: ""<br>SUBSEP: "\034"<br>TEXTDOMAIN: "messages"<br><br></td></tr></tbody></table>

* # FIELDS

     * If you are familiar with the Unix/Linux or do [bash shell programming](https://www.google.com/url?q=https://www.tecmint.com/category/bash-shell/&sa=D&ust=1555580831261000), then you should know what internal field separator (IFS) variable is. The default IFS in Awk are tab and space.

     * $1 $2 $3 …..

 * ## Example

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td># cat test.txt<br>Hare krishna hare krishna<br><br>$ awk '//{print $1 $2 $3 }' test.txt<br>Harekrishnahare<br><br>If you have noticed in the printed output, the field values are not separated and this is how print behaves by default.<br><br>$ awk '//{print $1, $2, $3; }' test.txt<br>Hare krishna hare<br></td></tr></tbody></table>

     * One important thing to note and always remember is that the use of ($) in Awk is different from its use in shell scripting.

     * Under shell scripting ($) is used to access the value of variables while in Awk ($) it is used only when accessing the contents of a field but not for accessing the value of variables.

     * Awk also has a printf command that helps you to format your output is a nice way as you can see the above output is not clear enough.

 * ## NF

     * NF is a predefined variable whose value is the number of fields in the current record.

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>This seems like a pretty nice example.<br></td></tr></tbody></table>

     * No matter how many fields there are, the last field in a record can be represented by $NF. So, $NF is the same as $7, which is ‘example.’

 * ## $0

     * The use of $0, which looks like a reference to the “zeroth” field, is a special case: it represents the whole input record. Use it when you are not interested in specific fields. 

 * ## EXAMPLE $1 and $0 and regex

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ awk '$1 ~ /li/ { print $0 }' mail-list<br>Amelia       555-5553     amelia.zodiacusque@gmail.com    F<br>Julie        555-6699     julie.perscrutabor@skeeve.com   F<br></td></tr></tbody></table>

     * This example prints each record in the file mail-list whose first field contains the string ‘li’.

     * By contrast, the following example looks for ‘li’ in the entire record and prints the first and last fields for each matching input record:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ awk '/li/ { print $1, $NF }' mail-list<br>Amelia F<br>Broderick R<br>Julie F<br>Samuel A<br></td></tr></tbody></table>

 * ## Nonconstant Field Numbers

     * A field number need not be a constant. Any expression in the awk language can be used after a ‘$’ to refer to a field. The value of the expression specifies the field number. If the value is a string, rather than a number, it is converted to a number. Consider this example:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>awk '{ print $NR }'<br></td></tr></tbody></table>

     * Recall that NR is the number of records read so far: one in the first record, two in the second, and so on. So this example prints the first field of the first record, the second field of the second record, and so on. For the twentieth record, field number 20 is printed; most likely, the record has fewer than 20 fields, so this prints a blank line. Here is another example of using expressions as field numbers:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>file1<br><br>1<br>1 2<br>1 2 3<br>1 2 3 4<br>1 2 3 4 5 <br><br>awk '{ print $NR }' file1 (NR is the number of records read so far)<br>1 (NR =1 so print $1)<br>2 (NR =2 so print $2 of 1 2)<br>3 (NR =3 so print $3 of 1 2 3)<br>4 (NR =4 so print $4 of 1 2 3 4)<br>5 (NR =5 so print $5 of 1 2 3 4 5)<br></td></tr></tbody></table>

     * As mentioned in [Fields](https://www.google.com/url?q=https://www.gnu.org/software/gawk/manual/html_node/Fields.html%23Fields&sa=D&ust=1555580831274000), awk stores the current record’s number of fields in the built-in variable NF (also see [Built-in Variables](https://www.google.com/url?q=https://www.gnu.org/software/gawk/manual/html_node/Built_002din-Variables.html%23Built_002din-Variables&sa=D&ust=1555580831274000)). Thus, the expression $NF is not a special feature—it is the direct consequence of evaluating NF and using its value as a field number.

 * ## Changing the Contents of a Field

     * The contents of a field, as seen by awk, can be changed within an awk program; this changes what awk perceives as the current input record. (The actual input is untouched; awk nevermodifies the input file.) Consider the following example and its output:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ awk '{ nboxes = $3 ; $3 = $3 - 10<br>&gt;        print nboxes, $3 }' inventory-shipped<br>25 15<br>32 22<br>24 14<br>…<br></td></tr></tbody></table>

     * The program first saves the original value of field three in the variable nboxes. The ‘-’ sign represents subtraction, so this program reassigns field three, $3, as the original value of field three minus ten: ‘$3 - 10’. (See [Arithmetic Ops](https://www.google.com/url?q=https://www.gnu.org/software/gawk/manual/html_node/Arithmetic-Ops.html%23Arithmetic-Ops&sa=D&ust=1555580831277000).) Then it prints the original and new values for field three. (Someone in the warehouse made a consistent mistake while inventorying the red boxes.)

     * When the value of a field is changed (as perceived by awk), the text of the input record is recalculated to contain the new field where the old one was. In other words, $0 changes to reflect the altered field. Thus, this program prints a copy of the input file, with 10 subtracted from the second field of each line:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ awk '{ $2 = $2 - 10; print $0 }' inventory-shipped<br>Jan 3 25 15 115<br>Feb 5 32 24 226<br>Mar 5 24 34 228<br>…<br></td></tr></tbody></table>

     * It is also possible to assign contents to fields that are out of range. For example:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ awk '{ $6 = ($5 + $4 + $3 + $2)<br>&gt;        print $6 }' inventory-shipped<br>168<br>297<br>301<br>…<br></td></tr></tbody></table>

     * We’ve just created $6, whose value is the sum of fields $2, $3, $4, and $5. The ‘+’ sign represents addition. For the file inventory-shipped, $6 represents the total number of parcels shipped for a particular month.

 * ## Example print last but one and last fields

     * |                                                               |

     * | ------------------------------------------------------------- |

     * | awk '{print $(NF - 1), $NF}' |

 * ## Example muliple print vs single print

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ echo "a b c d\n1 2 3 4" | awk '{print $0; print NF}'<br>a b c d<br>4<br>1 2 3 4<br>4<br><br>$ echo "a b c d\n1 2 3 4" | awk '{print $0, NF}'      <br>a b c d 4<br>1 2 3 4 4<br></td></tr></tbody></table>

* # HOW TO reconstitute the record

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$1 = $1   # force record to be reconstituted<br>print $0  # or whatever else with $0<br></td></tr></tbody></table>

     * It is important to remember that $0 is the full record, exactly as it was read from the input. This includes any leading or trailing whitespace, and the exact whitespace (or other characters) that separates the fields.

     * It is a common error to try to change the field separators in a record simply by setting FS and OFS, and then expecting a plain ‘print’ or ‘print $0’ to print the modified record.

     * But this does not work, because nothing was done to change the record itself. Instead, you must force the record to be rebuilt, typically with a statement such as ‘$1 = $1’, as described earlier.

     * Eg:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>echo a b c d e f | awk '{ print "NF =", NF; NF = 3; print $0 }'<br>NF = 6<br>a b c<br></td></tr></tbody></table>

     * CAUTION: Some versions of awk don’t rebuild $0 when NF is decremented

* # NR

     * NR is the number of records read so far

* # EXAMPLE OFS AND FS SET LATE, Setting of variables

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>&gt;Humanl|chr16:86430087-86430726 | element 1 | positive<br>&gt;Humanl|chr16:85620095-85621736 | element 2 | negative<br>&gt;Humanl|chr16:80423343-80424652 | element 3 | negative<br>&gt;Humanl|chr16:80372593-80373755 | element 4 | positive<br>&gt;Humanl|chr16:79969907-79971297 | element 5 | negative<br>&gt;Humanl|chr16:79949950-79951518 | element 6 | negative<br>&gt;Humanl|chr16:79026563-79028162 | element 7 | negative<br>&gt;Humanl|chr16:78933253-78934686 | element 9 | negative<br>&gt;Humanl|chr16:78832182-78833595 | element 10 | negative<br></td></tr></tbody></table>

     * TRIED

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>awk '{FS="|";OFS="\t"} {print $1,$2,$3,$4,$5}'<br></td></tr></tbody></table>

     * OUTPUT

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>&gt;Human|chr16:86430087-86430726  |      element 1      |<br>&gt;Human  chr16:85620095-85621736         element 2      negative<br>&gt;Human  chr16:80423343-80424652         element 3      negative<br>&gt;Human  chr16:80372593-80373755         element 4      positive<br>&gt;Human  chr16:79969907-79971297         element 5      negative<br>&gt;Human  chr16:79949950-79951518         element 6      negative<br>&gt;Human  chr16:79026563-79028162         element 7      negative<br>&gt;Human  chr16:78933253-78934686         element 9      negative<br>&gt;Human  chr16:78832182-78833595         element 10     negative<br></td></tr></tbody></table>

     * FAILED:  Every line works fine except for the first line. 

     * ANSWER:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>FS and OFS are set too late to affect the first line, use something like this instead:<br><br>awk '{print $1,$2,$3,$4,$5}' FS='|' OFS='\t'   ( append them after the script as VAR=VALUE. This is called post script variables)<br><br>You can also use this shorter version:<br><br>awk -v FS='|' -v OFS='\t' '$1=$1'  (using -v)<br><br>OR<br><br>awk 'BEGIN{FS="|";OFS="\t"} {print $1,$2,$3,$4,$5}'  (Using BEGIN)<br><br>Note that there is a significant difference between when -v and post-script variables are set. -v will set variables before the BEGIN clause whilst post-script setting of variables are set just after the BEGIN clause.<br></td></tr></tbody></table>

* # NR VS FNR

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ cat file1<br>a<br>b<br>c<br><br>$ cat file2<br>d<br>e<br><br>$ awk '{print FILENAME, NR, FNR, $0}' file1 file2<br>file1 1 1 a<br>file1 2 2 b<br>file1 3 3 c<br>file2 4 1 d<br>file2 5 2 e<br></td></tr></tbody></table>

     * Keep in mind NR and FNR are awk built-in variables. NR - Gives the total number of records processed. (in this case both in a.txt and b.txt) FNR - Gives the total number of records for each input file (records in either a.txt or b.txt)

     * This means that the condition NR==FNR is only true for the first file, as FNR resets back to 1 for the first line of each file but NR keeps on increasing.

* # EXAMPLE : Print number and File (NR vs count++)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ for file in **/*; do file $file; done|awk 'BEGIN {count=1} !/directory/{print count++" "$0}'<br>1 file1.txt: empty<br>2 file2.txt: empty<br>3 file3.txt: empty<br>4 test: directory<br>5 file4.txt: empty<br><br>NOTE: if we use NR instead of count and the counting will not be in sequence<br><br>$ for file in **/*; do file $file; done|awk ‘!/directory/{print NR" "$0}'<br>1 file1.txt: empty<br>2 file2.txt: empty<br>3 file3.txt: empty<br>5 file4.txt: empty<br></td></tr></tbody></table>

* # Example: find any field beginning from 2  which contains word image

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>for file in **/*; do file $file; done|awk 'BEGIN {count=0} !/directory/{for (i=2;i&lt;=NF;i++) {if ($i ~ /image/) {print count++,i,$i,$0}}}'<br></td></tr></tbody></table>

* # Example field

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>ls --full-time --time-style=+%Y-%m-%d-%H_%M_%S | awk '{print $6}'<br>2019-04-15-18_14_47<br>2019-04-15-18_14_47<br>2019-04-15-18_14_47<br>2019-04-15-18_14_47<br>2019-04-15-18_16_16<br>2019-04-09-01_56_41<br>2019-04-15-18_15_12<br></td></tr></tbody></table>

* # EXAMPLE OF IF and matching each field with \~:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ for file in **/*<br> do<br> f_base=`echo $file | awk 'BEGIN {FS="."} {a=""; for (i=1;i&lt;=NF;i++) {if (i==1) {a=$i;print i ":" a} else {a=a FS $i;print i ":" a}}; print a}'`;<br> echo $f_base<br> Done<br><br>1:file1  (printed by if (i==1) {a=$i;print i ":" a})<br>2:file1.txt  → printed by else {a=a FS $i;print i ":" a}<br>file1.txt   printed by print a<br>1:file2<br>2:file2.txt<br>file2.txt<br>1:file3<br>2:file3.txt<br>file3.txt<br>1:file4<br>2:file4.txt<br>file4.txt<br>1:hare<br>2:hare.txt<br>hare.txt<br>1:Harinaam_Monday_ISKCON_Chowpatty-qtFYjjo9LCc<br>2:Harinaam_Monday_ISKCON_Chowpatty-qtFYjjo9LCc.mkv<br>Harinaam_Monday_ISKCON_Chowpatty-qtFYjjo9LCc.mkv<br>1:test<br>test<br><br><br></td></tr></tbody></table>

* # RS

     * It represents (input)record separator and its default value is newline.

     * \[jerry\]$ awk 'BEGIN {print "RS = " RS}' | cat -vte

     * On executing the above code, you get the following result:

     * RS = $

     * $

* # $0

     * It represents the entire input record.

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>[jerry]$ awk '{print $0}' marks.txt<br><br>On executing the above code, you get the following result:<br><br>1)    Amit     Physics    80<br>2)    Rahul    Maths      90<br>3)    Shyam    Biology    87<br>4)    Kedar    English    85<br>5)    Hari     History    89<br></td></tr></tbody></table>

* # IGNORECASE

     * When this variable is set GAWK becomes case insensitive. Following simple example illustrates this:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>[jerry]$ awk 'BEGIN{IGNORECASE=1} /amit/' marks.txt<br><br>On executing the above code, you get the following result:<br><br>1)    Amit     Physics    80<br></td></tr></tbody></table>

* # EXAMPLE print

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>awk '$9 == 500 ' /var/log/httpd/access.log<br>awk '$9 == 500 {print} ' /var/log/httpd/access.log<br>awk '$9 == 500 {print $0} ' /var/log/httpd/access.log<br></td></tr></tbody></table>

* # REGEX NOT  MATCHING

     * Print only the lines that do not match a regular expression "/regex/" (emulates "grep -v").

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#guarangas<br>awk '!/regex/'<br><br>Example<br><br>Show all files which are not directories<br><br>for file in **; do file $file; done|awk '!/directory/{print NR" "$0}'<br><br>OR (the below gives the right results)<br><br>for file in **; do file $file; done|awk 'BEGIN {count=0} !/directory/{count++;print count" "$0}'<br><br></td></tr></tbody></table>

* # EXAMPLE find if contains words OR and AND

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>awk '/tom|jerry|vivek/' /etc/passwd<br><br>OR<br><br>awk '/tom/ || /jerry/ || /vivek/ {print}' /etc/passwd<br></td></tr></tbody></table>

* # Simply Arithmetic

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>You get the sum of all the numbers in a column:<br>awk '{total += $1} END {print total}' earnings.txt<br><br>Shell cannot calculate with floating point numbers, but awk can:<br>awk 'BEGIN {printf "%.3f\n", 2005.50 / 3}'<br></td></tr></tbody></table>

* # USE shell variable inside awk

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$gauranga<br>search="android"; awk -v r="$search"<br></td></tr></tbody></table>

* # EXAMPLE using function inside awk

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>awk 'function green(s) { printf "\033[1;32m" s "\033[0m "}; /Recycle/{print green($0)}' IGNORECASE=1 **/*.java (working)<br></td></tr></tbody></table>

* # EXAMPLE substituting in awk gsub

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ search="91+[0-9]"; awk -v r="$search" '{if($0 ~ r &amp;&amp; FNR==1){print "\n\033[1;31m"count++" : "FILENAME"\033[0m\n"; gsub(r,"\033[1;36m&amp;\033[1;000m"); print FNR":"$0} else if(FNR==1){check=0} else if($0 ~ r) {if(check==0){print "\n\033[1;31m"count++" :"FILENAME"\033[0m\n";gsub(r,"\033[1;36m&amp;\033[1;000m");print FNR":"$0;check=1} else {gsub(r,"\033[1;36m&amp;\033[1;000m");print FILENAME":"FNR":"$0}}}' IGNORECASE=1  .vlist<br><br>0 :.vlist<br><br>2:137        91xxxxxxxxxx        Mr. Vrajchandra Data<br>.vlist:3:342        91xxxxxxx        Mr. Vraj Das<br>.vlist:4:201        91xxxxxxxxxx        Mr. Hemant Thakur<br>.vlist:5:104        91xxxxxxxxx        Mr. Bankim Rayba Data<br>.vlist:6:234        91xxxxxxxxxx        Mr. Srikant Pool -GEV<br><br><br></td></tr></tbody></table>

* # EXAMPLE ADD new line after a line

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ awk '/android/;/android/{print "\n"}' IGNORECASE=1 .vlist<br><br>OR<br>$ awk '/android/{print;print "\n"}' IGNORECASE=1 .vlist<br><br><br>adb shell 'pm uninstall -k --user 0 com.sec.android.app.translator';<br><br><br>adb shell 'pm uninstall -k --user 0 com.sec.android.app.samsungapps';<br><br><br>adb shell 'pm uninstall -k --user 0 com.sec.android.app.kidshome';<br></td></tr></tbody></table>

* # passing shell variables

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>How do I pass shell variables to awk command or script under UNIX like operating systems?<br><br>The -v option can be used to pass shell variables to awk command. Consider the following simple example,<br><br><br>root="/webroot"<br>echo | awk -v r=$root '{ print "shell root value - " r}'<br><br><br>In this example search file using awk as follows:<br></td></tr></tbody></table>

* # EXAMPLE How to adding all the numbers in 4th column and print the total value at the end.

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>awk 'BEGIN{s=0}{s=s+$3}END{print s}' db.txt<br><br>Output:<br><br>297<br></td></tr></tbody></table>

* # How do I print all lines that have three (3) words only?

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>The awk command is well suitable for this kind of pattern processing text file. Awk set the variable called NF. It is set to the total number of fields in the input record. So if NF equal to three print the line. The syntax is as follows:<br><br>awk '{ if ( NF == 3 ) print } ' /path/to/input<br></td></tr></tbody></table>

* # EXAMPLE Gsub

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Create a data file cat /tmp/data.txt<br><br>foo     bar 12,300.50<br>foo bar 2,300.50<br>abc xyz 1,22,300.50<br><br>Type the following awk command:<br><br><br>awk '{ gsub(",","",$3); print $3 }' /tmp/data.txt<br><br><br>Sample outputs:<br><br>12300.50<br>2300.50<br>122300.50<br></td></tr></tbody></table>

* # EXAMPLE Processing the delimited files using awk

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>You can also use awk command for same purpose:<br>$ awk -F':' '{ print $1 }' /etc/passwd<br><br>Output:<br><br>root<br>you<br>me<br>vivek<br>httpd<br><br>Where,<br><br>-F: - Use : as fs (delimiter) for the input field separator<br>print $1 - Print first field, if you want print second field use $2 and so on<br></td></tr></tbody></table>

* # \*\* EXAMPLE The default syntax to read a text file line-by-line using awk is as follows:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>### note '{ print }' '{ print $0 }' '1' all are same ###<br>awk '{ print }' /path/to/file<br>awk '{}1' /path/to/file<br>awk '1' /path/to/file<br>awk '{ print $0 }' /path/to/file<br>awk '{}1' /etc/passwd<br>awk '{print $0}' /etc/hosts<br>awk '{print}' /etc/hosts<br><br>awk '{ print $1 }' filename<br><br><br>To see first and fourth fields of the current record, enter:<br><br><br>awk '{ print $1, $3 }' filename<br><br>The commands "print" and "print $0" are identical in functionality.<br></td></tr></tbody></table>

* # \*\* EXAMPLE awk define and print variable

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Create a variable called x and y:<br><br>awk 'BEGIN{x=3; y=4;}END{ print "x=" x " and y=" y}'&lt;/dev/null<br></td></tr></tbody></table>

* # \*\*EXAMPLE display line number

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>awk '{ print FNR " " $0 }' file<br>awk '{ print FNR " " $0 }' /etc/hosts<br>awk '{ print FNR "\t" $0 }' /etc/hosts<br></td></tr></tbody></table>

* # EXAMPLE print required lines

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Print 42nd line using awk command<br><br>awk "NR==42{print;exit}" filename<br><br>OR print 13 to 42 lines:<br><br>awk "NR&gt;=13{print} NR==42{exit}" /etc/passwd<br><br>Print 1 to 5 lines and number it on screen:<br><br>awk "NR&gt;=1{print} NR==5{exit}" /etc/group | cat -n<br></td></tr></tbody></table>

* # Here are some ways to get variables in to awk:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>You can use variable within the awk code, but its messy and hard to read:<br><br>variable="line one\nline two"<br>awk 'BEGIN {print "'"$variable"'"}'<br>line one<br>line two<br><br>variable="line one\nline two"; awk 'BEGIN {print "'"$variable"'"}'<br><br>variable="line one\nline two"; awk -v hare="$variable" 'BEGIN {print hare}' <br><br>This is the best way to do it is using -v option: (PS use space after -v or it will be less portable. Eks awk -v var= not awk -vvar)<br><br>awk -v var="$variable" 'BEGIN {print var}'<br>line one<br>line two<br><br>If you use variable in BEGIN block, it must be read with -v before BEGIN block.<br><br>To use variable elsewhere in awk you can read it after code like this:<br><br>echo "input data" | awk '{print var}' var="$variable"<br>or<br>awk '{print var}' var="$variable" file<br></td></tr></tbody></table>

* # \*\* spliting into files

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>awk '/XYZ/{a=$0}{if (a!="") print &gt; a;}'  sb_full.txt<br></td></tr></tbody></table>

* # Conditional awk printing

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>The awk syntax is as follows:<br><br><br>awk 'condition { action }' filename<br>awk '1 == /match/ { action }' filename<br>awk '1 == /match/ { print $0 }' filename<br>awk 'pattern { action }' filename<br><br><br>If first field match to vivek print the entire line:<br>$ awk -F: '1 == /vivek/ { print $0}' /etc/passwd<br><br>OR,<br><br>$ awk -F: '/vivek/ { print $0}' /etc/passwd (if we use this it will search the match in the whole line<br></td></tr></tbody></table>

* # passing variable: Correct, awk won't recogize variables in / /. You can do:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Name="jony"<br>awk -v name="$Name" '$0 ~ name' file<br><br>Since print is awk's default behavior we can avoid using it here.<br></td></tr></tbody></table>

* #   awk - Match a pattern in a file in Linux:  

     * \~ is the symbol used for pattern matching.  The / / symbols are used to specify the pattern.

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>  In one of our earlier articles on awk series, we had seen the basic usage of awk or gawk. In this, we will see mainly how to search for a pattern in a file in awk. Searching pattern in the entire line or in a specific column.<br><br>  Let us consider a csv file with the following contents. The data in the csv file contains kind of expense report. Let us see how to use awk to filter data from the file.<br><br>$ cat file<br>Medicine,200<br>Grocery,500<br>Rent,900<br>Grocery,800<br>Medicine,600<br><br>1. To print only the records containing Rent:<br><br>$ awk '$0 ~ /Rent/{print}' file<br>Rent,900<br><br>     ~ is the symbol used for pattern matching.  The / / symbols are used to specify the pattern. The above line indicates: If the line($0) contains(~) the pattern Rent, print the line. 'print' statement by default prints the entire line. This is actually the simulation of grep command using awk.<br><br>2. awk, while doing pattern matching, by default does on the entire line, and hence $0 can be left off as shown below:<br><br>$ awk '/Rent/{print}' file<br>Rent,900<br><br>3. Since awk prints the line by default on a true condition, print statement can also be left off.<br><br>$ awk '/Rent/' file<br>Rent,900<br><br> In this example, whenever the line contains Rent, the condition becomes true and the line gets printed.<br><br>4. In the above examples, the pattern matching is done on the entire line, however, the pattern we are looking for is only on the first column.  This might lead to incorrect results if the file contains the word Rent in other places. To match a pattern only in the first column($1),<br><br>$ awk -F, '$1 ~ /Rent/' file<br>Rent,900<br><br>      The -F option in awk is used to specify the delimiter. It is needed here since we are going to work on the specific columns which can be retrieved only when the delimiter is known.<br><br>5. The above pattern match will also match if the first column contains "Rents". To match exactly for the word "Rent" in the first column:<br><br>$ awk -F, '$1=="Rent"' file<br>Rent,900<br><br>6. To print only the 2nd column for all "Medicine" records:<br><br>$ awk -F, '$1 == "Medicine"{print $2}' file<br>200<br>600<br><br>7. To match for patterns "Rent" or "Medicine" in the file:<br><br>$ awk '/Rent|Medicine/' file<br>Medicine,200<br>Rent,900<br>Medicine,600<br><br>8. Similarly, to match for this above pattern only in the first column:<br><br>$ awk -F, '$1 ~ /Rent|Medicine/' file<br>Medicine,200<br>Rent,900<br>Medicine,600<br><br>9. What if the the first column contains the word "Medicines". The above example will match it as well. In order to exactly match only for Rent or Medicine,<br><br>$ awk -F, '$1 ~ /^Rent$|^Medicine$/' file<br>Medicine,200<br>Rent,900<br>Medicine,600<br><br>    The ^ symbol indicates beginning of the line, $ indicates the end of the line. ^Rent$ matches exactly for the word Rent in the first column, and the same is for the word Medicine as well.<br><br>10. To print the lines which does not contain the pattern Medicine:<br><br>$ awk '!/Medicine/' file<br>Grocery,500<br>Rent,900<br>Grocery,800<br><br>    The ! is used to negate the pattern search.<br><br>11. To negate the pattern only on the first column alone:<br><br>$ awk -F, '$1 !~ /Medicine/' file<br>Grocery,500<br>Rent,900<br>Grocery,800<br><br>12. To print all records whose amount is greater than 500:<br><br>$ awk -F, '$2&gt;500' file<br>Rent,900<br>Grocery,800<br>Medicine,600<br><br>13. To print the Medicine record only if it is the 1st record:<br><br>$ awk 'NR==1 &amp;&amp; /Medicine/' file<br>Medicine,200<br><br>    This is how the logical AND(&amp;&amp;) condition is used in awk.  The records needed to be retrieved is only if it is the first record(NR==1) and the record is a medicine record.<br><br>14. To print all those Medicine records whose amount is greater than 500:<br><br>$ awk -F, '/Medicine/ &amp;&amp; $2&gt;500' file<br>Medicine,600<br><br>15. To print all the Medicine records and also those records whose amount is greater than 600:<br><br>$ awk -F, '/Medicine/ || $2&gt;600' file<br>Medicine,200<br>Rent,900<br>Grocery,800<br>Medicine,600<br><br></td></tr></tbody></table>

* # To get color output from awk, you can use this approach.

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>function red(s) {<br>printf "\033[1;31m" s "\033[0m "<br>}<br><br>function green(s) {<br>printf "\033[1;32m" s "\033[0m "<br>}<br><br>function blue(s) {<br>printf "\033[1;34m" s "\033[0m "<br>}<br><br>{<br>print red($1), green($2), blue($3)<br>}<br></td></tr></tbody></table>

* # AWK colors and ANSI graphics 

     * ANSI code has always been pretty much of a minority interest and

     * (slightly old fashioned) black art, but it is useful & can be

     * very effective in conjunction with Awk.  This FAQ just covers the

     * graphics parameters that allow coloured text, reverse video etc -

     * it does not cover the parameters which control the cursor movement

     * and on screen placement.

     * ANSI graphics parameters take the form

     * ESC\[att;attm

     * where 'ESC' is the escape, 'att' represents one or more attributes

     * separated by ';' and 'm' terminates the code.  In Linux (Unix) the

     * escape is \\033, so:

     * echo -e '\\033\[5;41;1;37m    \*\*\* STOP \*\*\*    \\033\[0m'

     * will print the flashing message '    \*\*\* STOP \*\*\*    ' in bright white

     * letters on a red background.  The instruction '\\033\[0m' turns off all

     * attributes and returns the screen to its normal appearance.

* # EXAMPLE OFS

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>To print the first and third columns, ie., the name and the expertise:<br><br>$ awk -F"," '{print $1, $3}' file1<br>Name Expertise<br>Deepak MQ Series<br>Neha Power Builder<br>Vijay CRM Expert<br>Guru Unix<br><br>10. The output shown above is not easily readable since the third column has more than one word. It would have been better had the fields being displayed are present with a delimiter. Say, lets use comma to separate the output. Also, lets discard the header record.<br><br>$ awk -F"," 'NR!=1{print $1,$3}' OFS="," file1<br>Deepak,MQ Series<br>Neha,Power Builder<br>Vijay,CRM Expert<br>Guru,Unix<br><br>  OFS is another awk special variable. Just like how FS is used to separate the input fields, OFS (Output field separator) is used to separate the output fields. <br></td></tr></tbody></table>

* # How do we get the entire file content printed in other way?

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ awk '1' file1<br>Name Domain<br>Deepak Banking<br>Neha Telecom<br>Vijay Finance<br>Guru Migration<br><br>   The above awk command has only the pattern or condition part, no action part. The '1' in the pattern indicates "true" which means true for every line. As said above, no action part denotes just to print which is the default when no action statement is given, and hence the entire file contents get printed.<br></td></tr></tbody></table>

* # How to omit the header record and get only the names printed?

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ awk 'NR!=1{print $1}' file1<br>Deepak<br>Neha<br>Vijay<br>Guru<br><br>    The above awk command uses a special variable NR. NR denotes line number ranging from 1 to the actual line count. The conditon 'NR!=1' indicates not to execute the action part for the first line of the file, and hence the header record gets skipped.<br></td></tr></tbody></table>

* #  awk - Match a pattern in a file in Linux

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>  In one of our earlier articles on awk series, we had seen the basic usage of awk or gawk. In this, we will see mainly how to search for a pattern in a file in awk. Searching pattern in the entire line or in a specific column.<br><br>  Let us consider a csv file with the following contents. The data in the csv file contains kind of expense report. Let us see how to use awk to filter data from the file.<br><br>$ cat file<br>Medicine,200<br>Grocery,500<br>Rent,900<br>Grocery,800<br>Medicine,600<br><br>1. To print only the records containing Rent:<br><br>$ awk '$0 ~ /Rent/{print}' file<br>Rent,900<br><br>     ~ is the symbol used for pattern matching.  The / / symbols are used to specify the pattern. The above line indicates: If the line($0) contains(~) the pattern Rent, print the line. 'print' statement by default prints the entire line. This is actually the simulation of grep command using awk.<br><br>2. awk, while doing pattern matching, by default does on the entire line, and hence $0 can be left off as shown below:<br><br>$ awk '/Rent/{print}' file<br>Rent,900<br><br>3. Since awk prints the line by default on a true condition, print statement can also be left off.<br><br>$ awk '/Rent/' file<br>Rent,900<br><br> In this example, whenever the line contains Rent, the condition becomes true and the line gets printed.<br><br>4. In the above examples, the pattern matching is done on the entire line, however, the pattern we are looking for is only on the first column.  This might lead to incorrect results if the file contains the word Rent in other places. To match a pattern only in the first column($1),<br><br>$ awk -F, '$1 ~ /Rent/' file<br>Rent,900<br><br>      The -F option in awk is used to specify the delimiter. It is needed here since we are going to work on the specific columns which can be retrieved only when the delimiter is known.<br><br>5. The above pattern match will also match if the first column contains "Rents". To match exactly for the word "Rent" in the first column:<br><br>$ awk -F, '$1=="Rent"' file<br>Rent,900<br><br>6. To print only the 2nd column for all "Medicine" records:<br><br>$ awk -F, '$1 == "Medicine"{print $2}' file<br>200<br>600<br><br>7. To match for patterns "Rent" or "Medicine" in the file:<br><br>$ awk '/Rent|Medicine/' file<br>Medicine,200<br>Rent,900<br>Medicine,600<br><br>8. Similarly, to match for this above pattern only in the first column:<br><br>$ awk -F, '$1 ~ /Rent|Medicine/' file<br>Medicine,200<br>Rent,900<br>Medicine,600<br><br>9. What if the the first column contains the word "Medicines". The above example will match it as well. In order to exactly match only for Rent or Medicine,<br><br>$ awk -F, '$1 ~ /^Rent$|^Medicine$/' file<br>Medicine,200<br>Rent,900<br>Medicine,600<br><br>    The ^ symbol indicates beginning of the line, $ indicates the end of the line. ^Rent$ matches exactly for the word Rent in the first column, and the same is for the word Medicine as well.<br><br>10. To print the lines which does not contain the pattern Medicine:<br><br>$ awk '!/Medicine/' file<br>Grocery,500<br>Rent,900<br>Grocery,800<br><br>    The ! is used to negate the pattern search.<br><br>11. To negate the pattern only on the first column alone:<br><br>$ awk -F, '$1 !~ /Medicine/' file<br>Grocery,500<br>Rent,900<br>Grocery,800<br><br>12. To print all records whose amount is greater than 500:<br><br>$ awk -F, '$2&gt;500' file<br>Rent,900<br>Grocery,800<br>Medicine,600<br><br>13. To print the Medicine record only if it is the 1st record:<br><br>$ awk 'NR==1 &amp;&amp; /Medicine/' file<br>Medicine,200<br><br>    This is how the logical AND(&amp;&amp;) condition is used in awk.  The records needed to be retrieved is only if it is the first record(NR==1) and the record is a medicine record.<br><br>14. To print all those Medicine records whose amount is greater than 500:<br><br>$ awk -F, '/Medicine/ &amp;&amp; $2&gt;500' file<br>Medicine,600<br><br>15. To print all the Medicine records and also those records whose amount is greater than 600:<br><br>$ awk -F, '/Medicine/ || $2&gt;600' file<br>Medicine,200<br>Rent,900<br>Grocery,800<br>Medicine,600<br></td></tr></tbody></table>

* # 3. awk has the getline command which reads the next line from the file.

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ awk '/Linux/{print;getline;print;}' file<br>Linux<br>Solaris<br><br>Once the line containing the pattern Linux is found, it is printed. getline command reads the next line into $0. Hence, the second print statement prints the next line in the file.<br><br>4. In this, the same thing is achieved using only one print statement.<br><br>$ awk '/Linux/{getline x;print $0 RS x;}' file<br>Linux<br>Solaris<br><br> getline x reads the next line into variable x. x is used in order to prevent the getline from overwriting the current line present in $0. The print statement prints the current line($0), record separator(RS) which is the newline, and the next line which is in x. - See more at: http://www.theunixschool.com/2012/05/different-ways-to-print-next-few-lines.html#sthash.1DZYmvl6.dpuf<br></td></tr></tbody></table>

* # o print only the line following the pattern without the line matching the pattern:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Same using awk:<br><br>$ awk '/Linux/{getline;print;}' file<br>Solaris<br><br>- See more at: http://www.theunixschool.com/2012/05/different-ways-to-print-next-few-lines.html#sthash.1DZYmvl6.dpuf<br></td></tr></tbody></table>

* # Print multiple lines are selecting

     * $ awk '$2=="KFC" {print; for(i=1; i\<=4; i++) { getline; print}}' example.txt

     * Restaurant: KFC

     * City: NYC

     * State: NY

     * Address: 123 Madison Square

     * Phone: 911

     * The above command will get and print the consecutive 4 lines along with the current line because it was fed into a for loop.The search pattern $2=="KFC" will helps to get a particular line from the multiple lines.

* # Gsub vs sub

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Use gsub which does global substitution:<br>echo This++++this+++is+not++done | awk '{gsub(/\++/," ");}1'<br>sub function replaces only 1st match, to replace all matches use gsub.<br>OR<br>echo "This++++this+++is+not++done" | sed -re 's/(\+)+/ /g'<br></td></tr></tbody></table>

* # AWK: the substr command to select a substring

     * substr(s, a, b) : it returns b number of chars from string s, starting at position a. The parameter b is optional, in which case it means up to the end of the string.

     * Example:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>every good<br><br>Let us save this data into a file called data.txt<br>Then, here are a few case examples:<br><br>Shell<br>awk '{print substr($1,1,1)}' data.txt   #returns e<br>awk '{print substr($1,3)   }' data.txt   #returns ery<br>awk '{print substr($2,3)   }' data.txt   #returns od<br>awk '{print substr($0,7,2) }' data.txt  #returns go<br></td></tr></tbody></table>

     * Example 2:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Addr:192.168.1.135<br><br>awk '{print substr(column-number,start-point,end-point)}'<br><br>$ ifconfig eth0 | awk '/inet addr/{print substr($2,6)}'<br>192.168.1.135<br><br>$ ifconfig eth0 | awk '/inet addr/{print substr($2,6,3)}'<br>192<br></td></tr></tbody></table>

* # Match function

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ awk 'BEGIN {<br>   str = "      * In django we generall do migration after creating a django project and configuring the database in settings.py. Also ./manage.py runserver  shows warning that migrations are pending. Basically there are many applications which are mentioned in INSTALLED APPS which need to setup their tables in database."<br>   subs = "Two"<br>   ret = match(str,/^(\s*(\S)\s*)(.*)/,a)<br>   print "a[1]::" a[1]<br>   print "a[2]::"a[2]<br>   print "a[3]::" a[3]<br>   print "RLENGTH::"RLENGTH<br>   print "RSTART::"RSTART<br>}'<br><br>a[1]::      * <br>a[2]::*<br>a[3]::In django we generall do migration after creating a django project and configuring the database in settings.py. Also ./manage.py runserver  shows warning that migrations are pending. Basically there are many applications which are mentioned in INSTALLED APPS which need to setup their tables in database.<br>RLENGTH::312<br>RSTART::1<br></td></tr></tbody></table>

* # EXAMPLE EXIT AFTER 1st RECORD

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ awk '/\* #[^#]/{print}' README.md <br>* # Django Documentation:<br>* # 1.NEVER DO FIRST MIGRATION WITHOUT CREATING A CUSTOM “USER” MODEL and setting AUTH\_USER\_MODEL = custom\_user.User in Settings.py<br>* # 2. NEVER UPGRADE POSTGRESQL WITHOUT TAKING BACKUP. <br>* # Github Documentation using MarkDown:<br>* # FIRST COMMIT START<br>* # FIRST COMMIT END<br>* # SECOND COMMIT START<br>* # SECOND COMMIT END<br>* # THIRD COMMIT START<br>* # THIRD COMMIT END<br>* # FOURTH COMMIT THEORY START<br>* # FOURTH COMMIT THEORY END<br>* # FOURTH COMMIT START<br>* # FOURTH COMMIT END<br><br> simha  ~/DOC_django_basic<br>$ awk '/\* #[^#]/{print;exit}' README.md<br>* # Django Documentation:<br><br><br></td></tr></tbody></table>

* # AWK: Access captured group from line pattern

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td><br><br>With gawk, you can use the match function to capture parenthesized groups.<br><br>gawk 'match($0, pattern, ary) {print ary[1]}' <br><br>example:<br><br>echo "abcdef" | gawk 'match($0, /b(.*)e/, a) {print a[1]}' <br><br>outputs cd.<br><br>Note the specific use of gawk which implements the feature in question.<br><br>For a portable alternative you can achieve similar results with match() and substr.<br><br>example:<br><br>echo "abcdef" | awk 'match($0, /b[^e]*/) {print substr($0, RSTART+1, RLENGTH-1)}'<br><br>outputs cd.<br><br><br></td></tr></tbody></table>

* # EXAMPLE awk print 

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>NODE_1<br>port 1<br>description blah<br>port 2<br>description blah blah<br>NODE_2<br>port 1<br>description blah<br>port 2<br>description blah<br>NODE_3<br>port 1<br>port 2<br>NODE_4<br>port 1<br>port 2<br>NODE_5<br>port 1<br>port 2<br>NODE_6<br>port 1<br>description blahdy blah<br>port 2<br>description floop-a-doop<br><br></td></tr></tbody></table>

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>awk '/^port/{port=$0}/^description/{print port;print $0}' nodes<br>port 1<br>description blah<br>port 2<br>description blah blah<br>port 1<br>description blah<br>port 2<br>description blah<br>port 1<br>description blahdy blah<br>port 2<br>description floop-a-doop<br><br></td></tr></tbody></table>

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>awk '/^NODE/{print $0}/^port/{port=$0}/^description/{print port;print $0}' nodes<br>NODE_1<br>port 1<br>description blah<br>port 2<br>description blah blah<br>NODE_2<br>port 1<br>description blah<br>port 2<br>description blah<br>NODE_3<br>NODE_4<br>NODE_5<br>NODE_6<br>port 1<br>description blahdy blah<br>port 2<br>description floop-a-doop<br><br></td></tr></tbody></table>

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>That description is actually wrong. What you want is: "If the line after port isn't description<br>don't print node and port either."<br>Code:<br>awk '/^NODE/{node=$0}/^port/{port=$0}/^description/{if(prev!=node){print node};print port;print $0;prev=node}' nodesNODE_1<br>port 1<br>description blah<br>port 2<br>description blah blah<br>NODE_2<br>port 1<br>description blah<br>port 2<br>description blah<br>NODE_6<br>port 1<br>description blahdy blah<br>port 2<br>description floop-a-doop<br><br><br><br>The c-syntax<br><br>While read (filename, line){<br>NR++<br>If ($0 ~ '/^NODE/){<br>node=$0<br>}<br>If ($0 ~ /^port/){<br>port=$0<br>}<br><br>…<br><br>}<br></td></tr></tbody></table>

* # EAMPLE print array of match

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Txt file:<br><br>NODE_1<br>port 1<br>description blah<br>port 2<br>description blah blah<br>NODE_2<br>port 1<br>description blah<br>port 2<br>description blah<br>NODE_3<br>port 1<br>port 2<br>NODE_4<br>port 1<br>port 2<br>NODE_5<br>port 1<br>port 2<br>NODE_6<br>port 1<br>description blahdy blah<br>port 2<br>description floop-a-doop<br><br><br>    awk 'BEGIN{count=0}<br>        match($0,/NODE/,a)<br>        {      &lt;-- matters (use it above for not printing the matched line)<br>        if(RSTART != 0){<br>            print "*******************************"<br>            for (i in a)<br>            print i"--&gt;"a[i]<br>            count++;<br>            print "count--&gt;"count;    <br>            print "*******************************"<br>            }<br>        if (count &gt;= 3)<br>            {<br>            exit<br>            }<br>        }' awksampledata5.txt<br><br><br>NODE_1<br>*******************************<br>0start--&gt;1<br>0length--&gt;4<br>0--&gt;NODE<br>count--&gt;1<br>*******************************<br>NODE_2<br>*******************************<br>0start--&gt;1<br>0length--&gt;4<br>0--&gt;NODE<br>count--&gt;2<br>*******************************<br>NODE_3<br>*******************************<br>0start--&gt;1<br>0length--&gt;4<br>0--&gt;NODE<br>count--&gt;3<br>*******************************<br></td></tr></tbody></table>

     * EXAMPLE awk replace part of text with previous lines USED in README.md

     * We have to use match when we want to use regex groups.

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ awk 'BEGIN{<br>    count=0;<br>    prevNR=0;<br>    prevChar=""<br>    }<br>    match($0,/^(( +)(\*)( +))([^#].*)/,a){<br>        if(prevNR!=0 &amp;&amp; NR == prevNR+2){<br>            print prevChar a[5]<br>            prevNR = NR<br><br>        }<br>        else{<br>            print;<br>            prevChar = a[1];<br>            prevNR = NR<br>        }<br>    }<br><br>    !/^(( +)(\*)( +))([^#].*)/{<br>        print;<br>    }<br><br>    /^ +\* +#/{<br>            prevChar = "";<br>    }<br><br>    ' testread.md<br><br><br><br>convert :<br><br> * ## 2.Install the PostgreSQL Django adapter, psycopg2<br><br>     * &lt;table&gt;&lt;colgroup&gt;&lt;col style="width: 100%" /&gt;4<br><br>        * &lt;table&gt;&lt;colgroup&gt;&lt;col style="width: 100%" /&gt;&lt;/colgroup&gt;&lt;tbody&gt;1<br><br>    * &lt;table&gt;&lt;colgroup&gt;&lt;col style="width: 100%" /&gt;&lt;/colgroup&gt;&lt;tbody&gt;2<br><br>    * &lt;table&gt;&lt;colgroup&gt;&lt;col style="width: 100%" /&gt;&lt;/colgroup&gt;&lt;tbody&gt;3<br><br>to<br><br> * ## 2.Install the PostgreSQL Django adapter, psycopg2<br><br>     * &lt;table&gt;&lt;colgroup&gt;&lt;col style="width: 100%" /&gt;4<br><br>     * &lt;table&gt;&lt;colgroup&gt;&lt;col style="width: 100%" /&gt;&lt;/colgroup&gt;&lt;tbody&gt;1<br><br>     * &lt;table&gt;&lt;colgroup&gt;&lt;col style="width: 100%" /&gt;&lt;/colgroup&gt;&lt;tbody&gt;2<br><br>     * &lt;table&gt;&lt;colgroup&gt;&lt;col style="width: 100%" /&gt;&lt;/colgroup&gt;&lt;tbody&gt;3<br><br></td></tr></tbody></table>

     * EXAMPLE RS (RECORD SEPERATOR)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ gawk 'BEGIN {FS="\n" ; RS="here\n"} {printf "Row:%d Data:[%s %s %s]\n", NR, $1, $2, $3}' file<br>Row:1 Data:[1 2 3]<br>Row:2 Data:[a b c]<br></td></tr></tbody></table>

