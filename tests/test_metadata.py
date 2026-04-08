import unittest
from video_organizer.core.metadata import extract_metadata

class TestMetadataExtraction(unittest.TestCase):
    
    # --- PROS: What works perfectly ---

    def test_standard_movie(self):
        """Tests standard movie formats with years."""
        meta = extract_metadata("Inception.2010.1080p.mp4")
        self.assertEqual(meta.video_type, "Movie")
        self.assertEqual(meta.year, "2010")
        self.assertEqual(meta.language, "English")

    def test_movie_without_year(self):
        """Tests movies that don't have a year in the filename."""
        meta = extract_metadata("The_Matrix_Bluray.mkv")
        self.assertEqual(meta.video_type, "Movie")
        self.assertEqual(meta.year, "Unknown")
        self.assertEqual(meta.language, "English")
        
    def test_language_detection(self):
        """Tests basic language detection by keywords in filename."""
        meta1 = extract_metadata("Dangal.2016.HINDI.720p.mkv")
        self.assertEqual(meta1.video_type, "Movie")
        self.assertEqual(meta1.language, "Hindi")
        
        meta2 = extract_metadata("La.Casa.De.Papel.S03E01.Spanish.mkv")
        self.assertEqual(meta2.video_type, "Series")
        self.assertEqual(meta2.language, "Spanish")
        self.assertEqual(meta2.season, "Season 03")
        
    def test_standard_series_s01e01(self):
        """Tests standard S01E01 TV series formatting."""
        meta = extract_metadata("Breaking.Bad.S01E01.Pilot.mp4")
        self.assertEqual(meta.video_type, "Series")
        self.assertEqual(meta.series_name, "Breaking Bad")
        self.assertEqual(meta.season, "Season 01")
        
    def test_series_with_1x02_format(self):
        """Tests alternate 1x02 TV series formatting."""
        meta = extract_metadata("game.of.thrones.2x04.mkv")
        self.assertEqual(meta.video_type, "Series")
        self.assertEqual(meta.series_name, "Game Of Thrones")
        self.assertEqual(meta.season, "Season 02")

    # --- CONS/LIMITATIONS: What currently fails or falls back to 'Movie' ---

    def test_series_with_spelled_out_season(self):
        """
        LIMITATION: The current regex only matches 'S01E01' or '1x01'. 
        It does not match spelled out 'Season 1 Episode 1'.
        Therefore, this will fallback and be treated as a Movie.
        """
        meta = extract_metadata("The_Office_Season_1_Episode_1.avi")
        # Currently, this falls back to being identified as a Movie
        self.assertEqual(meta.video_type, "Movie") 
        self.assertEqual(meta.series_name, "")
        
    def test_movie_with_series_like_name(self):
        """
        LIMITATION: If a movie has something like '1x02' naturally in its title by coincidence,
        it might accidentally get classified as a Series.
        """
        meta = extract_metadata("Terminator.2.Judgment.Day.1991.1080p.2x01.mp4")
        # Due to '2x01' at the end, the parser will mistakenly think it's a TV Show.
        self.assertEqual(meta.video_type, "Series")

if __name__ == '__main__':
    unittest.main()
