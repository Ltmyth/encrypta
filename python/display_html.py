import os
import webbrowser

html = """
<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Encrypta</title> 
        <link rel="stylesheet" href="../css/style.css">
    </head>
    <body>
        <br><br><br>
        <h2>IMAGES & HISTOGRAMS</h2>
        <table class='images'>
            <tr>
                <th>Cover Image 1</th> 
                <th>Histogram of the Cover Image</th>
            </tr>
            <tr>
                <td>
                    <img src='../images/journey.png'>
                </td>
                <td>
                    <img src='../images/journey_histogram.png'>
                </td>
            </tr>
            <tr>
                <th>(LSB Encrypted)</th>
                <th>Histogram of the LSB Encrypted Image</th>
            </tr>
            <tr>
                <td>
                    <img src='../encrypted/lsb_encoded_journey.png'>
                </td>
                <td>
                    <img src='../images/journey_lsb_histogram.png'>
                </td>
            </tr>



            <tr>
                <th>Cover Image 2</th>
                <th>Histogram of the Cover Image</th>
            </tr>
            <tr>
                <td>
                    <img src='../images/girafe.png'>
                </td>
                <td>
                    <img src='../images/girafe_histogram.png'>
                </td>
            </tr>
            <tr>
                <th>(LSB Encrypted)</th>
                <th>Histogram of the LSB Encrypted Image</th>
            </tr>
            <tr>
                <td>
                    <img src='../encrypted/lsb_encoded_girafe.png'>
                </td>
                <td>
                    <img src='../images/girafe_lsb_histogram.png'>
                </td>
            </tr>



            <tr>
                <th>Cover Image 3</th>
                <th>Histogram of the Cover Image</th>
            </tr>
            <tr>
                <td>
                    <img src='../images/kids.png'>
                </td>
                <td>
                    <img src='../images/kids_histogram.png'>
                </td>
            </tr>
            <tr>
                <th> (LSB Encrypted)</th>
                <th>Histogram of the LSB Encrypted Image</th>
            </tr>
            <tr>
                <td>
                    <img src='../encrypted/lsb_encoded_kids.png'>
                </td>
                <td>
                    <img src='../images/kids_lsb_histogram.png'>
                </td>
            </tr>
        </table>
        <br><br><br><br><br>
        <h2>TIME </h2>
        <table>
            <tr>
                <th colspan="7"> Response Time in seconds</th>
            </tr>
            <tr>
                <th colspan="3">Cover Image</th>
                <th>Size</th>
                <th>LSB Encryption time</th>
                <th>LSB Decryption time</th>
                <th>Total LSB time</th>
            </tr>
            <tr>
                <td colspan="3">1</td>
                <td>1.2 MB</td>
                <td>6.618632</td>
                <td> 0.681449</td>
                <td> <b>7.300081</b></td>
            </tr>
            <tr>
                <td colspan="3">2</td>
                <td>2.9 MB</td>
                <td>12.194479</td>
                <td> 1.134509</td>
                <td> <b>13.328988</b></td>
            </tr>
            <tr>
                <td colspan="3">3</td>
                <td>7.2 MB</td>
                <td>31.071637</td>
                <td> 2.842029</td>
                <td>  <b>33.913666</b></td>
            </tr>

            <tr>
                <th colspan='7'> Message Encryption</th>
            </tr>
            <tr>
                <th>AES Encryption time</th>
                <th>AES Decryption time</th>
                <th>Total AES time time</th>
                <th>RSA Encryption time</th>
                <th>RSA Decryption time</th>
                <th>Total RSA time</th>
                <th> TOTAL TIME </th>
            </tr>
            <tr>
                <td>0.011895</td>
                <td>0.002815</td>
                <td><b>0.121765</b></td>
                <td> 0.502411</td>
                <td> 0.684402</td>
                <td><b>1.186813</b></td>
                <td><strong>1.308578</strong></td>
            </tr>
            
        </table>
    </body>
<html>
"""


path = os.path.abspath('html/display.html')
url = 'file://' + path

with open(path, 'w') as f:
    f.write(html)
webbrowser.open(url)