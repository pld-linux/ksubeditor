Summary:	Ksubeditor - a DivX subtitle editor for KDE 3.x
Summary(pl.UTF-8):	Ksubeditor - edytor napisów dla KDE 3.x
Name:		ksubeditor
Version:	0.2
Release:	7
Epoch:		2
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/ksubeditor/%{name}-%{version}.tar.gz
# Source0-md5:	ddfb1c2ad888127835df09e5479b438d
Patch0:		%{name}-desktop.patch
URL:		http://www.sourceforge.net/projects/ksubeditor/
BuildRequires:	automake
BuildRequires:	fam-devel
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ksubeditor is a DivX subtitle editor for KDE 3.x. It is able to edit
and convert subtitles between different subtitle formats. It is able
to easily change the time of the subtitle and fit it to the movie.

%description -l pl.UTF-8
Ksubeditor jest edytorem napisów dla KDE 3.x. Jest w stanie
modyfikować oraz konwertować napisy pomiędzy różnymi formatami. Może w
prosty sposób zmieniać czas napisów oraz dopasować je do filmu.

%prep
%setup -q
%patch0 -p1

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
cp -f /usr/share/automake/config.sub admin
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

install -d $RPM_BUILD_ROOT%{_desktopdir} 

mv -f $RPM_BUILD_ROOT%{_iconsdir}/{lo,hi}color
mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Applications/ksubeditor.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}

#%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

#%files -f %{name}.lang
%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/ksubeditor
%{_iconsdir}/hicolor/*/apps/*.png
%{_desktopdir}/ksubeditor.desktop
