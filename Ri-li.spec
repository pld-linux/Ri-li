Summary:	Ri-li arcade game
Summary(de.UTF-8):	Ri-li Arkade Spiel
Summary(pl.UTF-8):	Ri-li - gra zręcznościowa
Name:		Ri-li
Version:	2.0.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/ri-li/%{name}-%{version}.tar.bz2
# Source0-md5:	57a2ff50a0c704786da8adf61d78bf52
Source1:	%{name}.desktop
URL:		http://www.ri-li.org
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Full-featured, 8 languages: Arabic, Chinese, English, French, German,
Japanese, Russian, Spanish. Colorful animated wood engine, 40 levels
in this first version and 3 beautiful musics and many sound effects.

%description -l de.UTF-8
Vollunterstützt, 8 Sprachen: Arabisch, Chinesisch, Englisch,
Französisch, Deutsch, Japanisch, Russisch, Spanisch. Buntes lebendiges
Holz-Engine, 40 Levels in dieser ersten Version und 3 schöne
Begleitmusiken und viele tolle Töne.

%description -l pl.UTF-8
Dopracowana, posiadająca 8 wersji językowych (arabską, chińską,
angielską, francuską, niemiecką, japońską, rosyjską i hiszpańską) gra
zręcznościowa. Wyróżnia się kolorową-drewnopodobną animowaną grafiką,
posiada 40 poziomów, 3 ładne ścieżki dźwiękowe do wyboru oraz wiele
efektów dźwiękowych.

%prep
%setup -q

%build
%configure
touch gentoo/games-arcade/Ri-li/Ri-li-2.0.0-r1.ebuild
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
install data/Ri-li-icon-16x16.png $RPM_BUILD_ROOT%{_pixmapsdir}
install data/Ri-li-icon-32x32.png $RPM_BUILD_ROOT%{_pixmapsdir}
install data/Ri-li-icon-48x48.png $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS NEWS COPYING.Music COPYING
%attr(755,root,root) %{_bindir}/Ri_li
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/levels.dat
%{_datadir}/%{name}/sprites.dat
%{_datadir}/%{name}/Ri-li-icon-*.png
%{_datadir}/%{name}/*.ico
%{_datadir}/%{name}/Sounds
%{_datadir}/%{name}/language.*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}*.png
