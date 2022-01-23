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
                    <img src='../images/ugflag.jpg'>
                </td>
                <td>
                    <img src='../images/ugflag_histogram.jpg'>
                </td>
            </tr>
            <tr>
                <th>(AES Encrypted)</th>
                <th>Histogram of the Stego Image</th>
            </tr>
            <tr>
                <td>
                    <img src='../images/ugflag_aes_encoded.jpg'>
                </td>
                <td>
                    <img src='../images/ugflag_aes_histogram.jpg'>
                </td>
            </tr>
            <tr>
                <th>(RSA Encrypted)</th>
                <th>Histogram of the RSA Encrypted Image</th>
            </tr>
            <tr>
                <td>
                    <img src='../images/ugflag_rsa_encoded.jpg'>
                </td>
                <td>
                    <img src='../images/ugflag_rsa_histogram.jpg'>
                </td>
            </tr>
            <tr>
                <th>(LSB Encrypted)</th>
                <th>Histogram of the LSB Encrypted Image</th>
            </tr>
            <tr>
                <td>
                    <img src='../images/ugflag_lsb_encoded.png'>
                </td>
                <td>
                    <img src='../images/ugflag_lsb_histogram.jpg'>
                </td>
            </tr>

            <tr>
                <th>Cover Image 2</th>
                <th>Histogram of the Cover Image</th>
            </tr>
            <tr>
                <td>
                    <img src='../images/kla.jpeg'>
                </td>
                <td>
                    <img src='../images/kla_histogram.jpeg'>
                </td>
            </tr>
            <tr>
                <th>(AES Encrypted)</th>
                <th>Histogram of the Stego Image</th>
            </tr>
            <tr>
                <td>
                    <img src='../images/kla_aes_encoded.jpg'>
                </td>
                <td>
                    <img src='../images/kla_aes_histogram.jpeg'>
                </td>
            </tr>
            <tr>
                <th>(RSA Encrypted)</th>
                <th>Histogram of the RSA Encrypted Image</th>
            </tr>
            <tr>
                <td>
                    <img src='../images/kla_rsa_encoded.jpeg'>
                </td>
                <td>
                    <img src='../images/kla_rsa_histogram.jpg'>
                </td>
            </tr>
            <tr>
                <th>(LSB Encrypted)</th>
                <th>Histogram of the LSB Encrypted Image</th>
            </tr>
            <tr>
                <td>
                    <img src='../images/kla_lsb_encoded.png'>
                </td>
                <td>
                    <img src='../images/kla_lsb_histogram.jpg'>
                </td>
            </tr>

            <tr>
                <th>Cover Image 3</th>
                <th>Histogram of the Cover Image</th>
            </tr>
            <tr>
                <td>
                    <img src='../images/journey.jpg'>
                </td>
                <td>
                    <img src='../images/journey_histogram.jpg'>
                </td>
            </tr>
            <tr>
                <th>(AES Encrypted)</th>
                <th>Histogram of the Stego Image</th>
            </tr>
            <tr>
                <td>
                    <img src='../images/journey_aes_encoded.jpg'>
                </td>
                <td>
                    <img src='../images/journey_aes_histogram.jpg'>
                </td>
            </tr>
            <tr>
                <th>(RSA Encrypted)</th>
                <th>Histogram of the RSA Encrypted Image</th>
            </tr>
            <tr>
                <td>
                    <img src='../images/journey_rsa_encoded.jpg'>
                </td>
                <td>
                    <img src='../images/journey_rsa_histogram.jpg'>
                </td>
            </tr>
            <tr>
                <th> (LSB Encrypted)</th>
                <th>Histogram of the LSB Encrypted Image</th>
            </tr>
            <tr>
                <td>
                    <img src='../images/journey_lsb_encoded.png'>
                </td>
                <td>
                    <img src='../images/journey_lsb_histogram.jpg'>
                </td>
            </tr>
        </table>
        <br><br><br><br><br>
        <h2>TIME </h2>
        <table>
            <tr>
                <th colspan='6'> Response Time in seconds</th>
            </tr>
            <tr>
                <th>Cover Image</th>
                <th>Size</th>
                <th>AES Encryption</th>
                <th>RSA Encryption</th>
                <th>LSB Encryption</th>
                <th>Total time</th>
            </tr>
            <tr>
                <td>1</td>
                <td>2 KB</td>
                <td>0.587701</td>
                <td>0.141763</td>
                <td>1.685483</td>
                <td>2.414947</td>
            </tr>
            <tr>
                <td>3</td>
                <td>358 KB</td>
                <td>17.602551</td>
                <td>1.387254</td>
                <td>17.366625</td>
                <td>36.356430</td>
            </tr>
            <tr>
                <td>3</td>
                <td>1.2 MB</td>
                <td>567.535737</td>
                <td>8.923301</td>
                <td>169.088363</td>
                <td>745.547401</td>
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