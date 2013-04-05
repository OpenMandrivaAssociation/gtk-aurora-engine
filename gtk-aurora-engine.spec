%define libname %mklibname %{name}

Summary:	Aurora engine for Gtk 2.x
Group:		Graphical desktop/Other
Name:		gtk-aurora-engine
Version:	1.5.1
Release:	3
License:	GPLv2+
Url:		http://gnome-look.org/content/show.php/Aurora+Gtk+Engine?content=56438
Source0:	http://gnome-look.org/CONTENT/content-files/56438-aurora-%{version}.tar.bz2
Patch0:		animation.diff
BuildRequires:	gtk2-devel >= 2.12
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
%apply_patches

# Fix bug 56215:
sed -i 's/\(^.*odd_row_color.*\)/\#\1/' Aurora/gtk-2.0/gtkrc

%build
pushd aurora-1.5
export LDFLAGS="-lm"
%configure2_5x --enable-animation
%make
popd

%install
%__rm -rf %{buildroot}
%makeinstall_std -C aurora-1.5
%__mkdir -p %{buildroot}%{_datadir}/themes
cp -fr Aurora %{buildroot}%{_datadir}/themes/


%files
%doc aurora-1.5/README aurora-1.5/ChangeLog
%{_datadir}/themes/*

%files -n %{libname}
%{_libdir}/gtk-2.0/*/engines/*.*


%changelog
* Wed Dec 07 2011 Zé <ze@mandriva.org> 1.5.1-2
+ Revision: 738465
- fix build
- clean defattr, BR, clean section and mkrel
- rebuild

* Sat Apr 30 2011 Funda Wang <fwang@mandriva.org> 1.5.1-1
+ Revision: 661029
- fix bug56215
- new version 1.5.1

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5-4mdv2011.0
+ Revision: 610990
- rebuild

* Mon Dec 07 2009 Lev Givon <lev@mandriva.org> 1.5-3mdv2010.1
+ Revision: 474455
- Tweak gtkrc files to fix #56215.

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Jan 16 2009 Lev Givon <lev@mandriva.org> 1.5-1mdv2009.1
+ Revision: 330228
- Update to 1.5.

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.4-2mdv2009.0
+ Revision: 266991
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 15 2008 Lev Givon <lev@mandriva.org> 1.4-1mdv2009.0
+ Revision: 194210
- Update to 1.4.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 12 2007 Lev Givon <lev@mandriva.org> 1.2-3mdv2008.1
+ Revision: 108290
- Fix libname on x86_64.

* Mon Nov 12 2007 Lev Givon <lev@mandriva.org> 1.2-2mdv2008.1
+ Revision: 108067
- Put libraries in separate package.

* Mon Oct 29 2007 Lev Givon <lev@mandriva.org> 1.2-1mdv2008.1
+ Revision: 103296
- import gtk-aurora-engine


* Mon Oct 29 2007 Lev Givon <lev@mandriva.org> 1.2-1mdv2008.0
- Package for Mandriva.
