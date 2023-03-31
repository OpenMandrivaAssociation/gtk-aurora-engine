%define libname %mklibname %{name}

Summary:	Aurora engine for Gtk 2.x
Group:		Graphical desktop/Other
Name:		gtk-aurora-engine
Version:	1.5.1
Release:	13
License:	GPLv2+
Url:		http://gnome-look.org/content/show.php/Aurora+Gtk+Engine?content=56438
Source0:	http://gnome-look.org/CONTENT/content-files/56438-aurora-%{version}.tar.bz2
Patch0:		animation.diff
BuildRequires:	pkgconfig(gtk+-2.0)
Requires:	%{libname} = %{version}

%description
The goal of this theme is to provide a complete and consistent look
for Gtk. The theme aims to be very flexible in color choice, but
provide few other options otherwise. The theme includes some features
that do not seem to be available in other Gtk engines; it also allows
the theming of Gnome panel widgets.

%package -n %{libname}
Summary:    Library files for %{name}
Group:	    System/Libraries

%description -n %{libname}
Library files for %{name}.

%prep
%setup -qc %{name}-%{version}
tar xf *.tar.bz2
tar xf *.tar.gz
%autopatch -p1

# Fix bug 56215:
sed -i 's/\(^.*odd_row_color.*\)/\#\1/' Aurora/gtk-2.0/gtkrc

%build
pushd aurora-1.5
export LDFLAGS="-lm"
%configure2_5x --enable-animation
%make
popd

%install
%makeinstall_std -C aurora-1.5
mkdir -p %{buildroot}%{_datadir}/themes
cp -fr Aurora %{buildroot}%{_datadir}/themes/

%files
%doc aurora-1.5/README aurora-1.5/ChangeLog
%{_datadir}/themes/*

%files -n %{libname}
%{_libdir}/gtk-2.0/*/engines/*.*

