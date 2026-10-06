using System.IO;
using System.Windows;
using System.Windows.Media.Imaging;

namespace Lagerfeuer;

/// <summary>Eine Frame-Folge aus einem horizontalen Sprite-Sheet.</summary>
public sealed class Animation
{
    public BitmapSource[] Frames { get; }
    public int FrameMs { get; }
    public bool Loop { get; }

    public Animation(BitmapSource[] frames, int frameMs, bool loop)
    {
        Frames = frames;
        FrameMs = frameMs;
        Loop = loop;
    }

    /// <summary>Laedt Assets/&lt;file&gt; und schneidet es in Frames der Groesse frameW x frameH.</summary>
    public static Animation Load(string file, int frameW, int frameH, int frameMs, bool loop)
    {
        var path = Path.Combine(AppContext.BaseDirectory, "Assets", file);

        var sheet = new BitmapImage();
        sheet.BeginInit();
        sheet.UriSource = new Uri(path);
        sheet.CacheOption = BitmapCacheOption.OnLoad;
        sheet.EndInit();
        sheet.Freeze();

        int count = sheet.PixelWidth / frameW;
        var frames = new BitmapSource[count];
        for (int i = 0; i < count; i++)
        {
            var frame = new CroppedBitmap(sheet, new Int32Rect(i * frameW, 0, frameW, frameH));
            frame.Freeze();
            frames[i] = frame;
        }

        return new Animation(frames, frameMs, loop);
    }
}
